import time
import datetime
from Seller.models import *
from django.shortcuts import render,HttpResponseRedirect
from django.http import JsonResponse
from Seller.views import setPassword#分页
from Buyer.models import *
from alipay import AliPay

import logging
# collect=logging.getLogger("django")
"""

    后端校验买家邮箱密码
    校验功能视图函数
    
"""
def loginValid(fun):
    def inner(request,*args,**kwargs):
        cookie_user=request.COOKIES.get("username")
        session_user=request.session.get("username")
        if cookie_user and session_user and cookie_user==session_user:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/Buyer/login/")
    return inner

"""
    买家登录功能视图函数
    注册、登录、登出、主页面、base页
"""

def login(request):
    if request.method=="POST":
        buyer_password=request.POST.get("pwd")
        buyer_email=request.POST.get("email")
        if buyer_email:
            user=User.objects.filter(email=buyer_email).first()
            db_password=user.password
            password=setPassword(buyer_password)
            if db_password==password:
                response=HttpResponseRedirect("/Buyer/index/")
                response.set_cookie("username",user.username)
                response.set_cookie("user_id",user.id)
                request.session["username"]=user.username

                # collect.debug("%s is login"%user.username)

                return response

    return render(request,'buyer/login.html',locals())
def register(request):
    if request.method=="POST":
        buyer_username=request.POST.get("user_name")
        buyer_password=request.POST.get("pwd")
        buyer_email=request.POST.get("email")
        if buyer_email:
            user = User.objects.filter(email=buyer_email).first()
            if not user:
                new_user = User()
                new_user.email = buyer_email
                new_user.password = setPassword(buyer_password)
                new_user.save()
                return HttpResponseRedirect("/Buyer/login/")
            else:
                error_message = "邮箱已被注册，请登录"
        else:
            error_message = "邮箱不能为空"
    return render(request,'buyer/register.html',locals())



def logout(request):
    url=request.META.get("HTTP_REFERER","/Buyer/index/")
    response = HttpResponseRedirect(url)
    for key in request.COOKIES:
        response.delete_cookie(key)
        print("删除cookie",key)
    if request.session.get("username"):
        del request.session["username"]
    return response



def index(request):
    goods_type=Goods_type.objects.all()#获取所有类型
    result=[]
    for ty in goods_type:
        #按照生产日期对对应类型的商品进行排序
        all_type_good=ty.goods_set.order_by("-goods_pro_time")
        if len(all_type_good)>=4:#进行条件判断
            all_type_good=all_type_good[:4]
            result.append({"type":ty,"type_goods_list":all_type_good})
    return render(request,'buyer/index.html',locals())

def goods_list(request):
    """
    type 代表请求的类型
        t 按照类型查询
            keywords 必须是类型id
        k 是按照关键字查询
            keywords可以是任何东西
    keywords 代表请求的关键字

    """
    request_type=request.GET.get("type")#获取请求的类型t类型查询  k关键字查询
    keyword=request.GET.get("keywords")#查询的内容 t类型 k为类型id  k类型 k为关键字
    goods_list=[]
    if request_type=="t":
        if keyword:
            id=int(keyword)
            goods_type=Goods_type.objects.get(id=id)#先查询类型
            goods_list=goods_type.goods_set.order_by("-goods_pro_time")#在查询类型对应的商品
    elif request_type=="k":
        if keyword:
            goods_list=Goods.objects.filter(goods_name__contains=keyword).order_by("-goods_pro_time")#模糊查询商品名称含有关键字的商品
    if goods_list:#限定推荐的条数
        lenth=len(goods_list)/5
        if lenth!=int(lenth):
            lenth+=1
        lenth=int(lenth)
        recommend=goods_list[:lenth]
    return render(request,'buyer/goods_list.html',locals())

#ajax功能
def goods_details(request,id):
    goods=Goods.objects.get(id=int(id))
    return render(request,'buyer/goods_details.html',locals())
@loginValid
def user_center_info(request):
    user_id=request.COOKIES.get("user_id")
    user=User.objects.get(id=int(user_id))
    return render(request,'buyer/user_center_info.html',locals())


"""
    支付功能视图函数
"""
@loginValid
def pay_order(request):
    goods_id=request.GET.get("goods_id")
    count=request.GET.get("count")
    if goods_id and count:
        #保存订单表，但是保存总价
        order=PayOrder()
        order.order_number=str(time.time()).replace(".","")
        order.order_data=datetime.datetime.now()
        order.order_status=0
        order.order_user=User.objects.get(id=int(request.COOKIES.get("user_id")))#订单对应买家
        order.save()
        #保存订单详情
        #查询商品的信息
        goods=Goods.objects.get(id=int(goods_id))
        order_info=OrderInfo()
        order_info.order_id=order
        order_info.goods_id=goods_id
        order_info.goods_picture=goods.picture
        order_info.goods_name=goods.goods_name
        order_info.goods_count=int(count)
        order_info.goods_price=goods.goods_price
        order_info.goods_total_price=goods.goods_price*int(count)
        order_info.store_id=goods.goods_store#商家卖家，goods.goods_store本身就是一条卖家数据
        order_info.save()
        order.order_total=order_info.goods_total_price
        order.save()

    return render(request,'buyer/pay_order.html',locals())

@loginValid
def pay_order_more(request):
    data=request.GET
    data_item=data.items()
    request_data=[]
    for key,value in data_item:
        if key.startswith("check_"):
            goods_id=key.split("_",1)[1]
            count=data.get("count_"+goods_id)
            request_data.append((int(goods_id),int(count)))
    if request_data:
        #保存订单表，但是保存总价
        order=PayOrder()
        order.order_number=str(time.time()).replace(".","")
        order.order_data=datetime.datetime.now()
        order.order_status=0
        order.order_user=User.objects.get(id=int(request.COOKIES.get("user_id")))#订单对应买家
        order.save()
        #保存订单详情
        #查询商品的信息
        order_total=0
        for goods_id,count in request_data:
            goods=Goods.objects.get(id=int(goods_id))
            order_info=OrderInfo()
            order_info.order_id=order
            order_info.goods_id=goods_id
            order_info.goods_picture=goods.picture
            order_info.goods_name=goods.goods_name
            order_info.goods_count=int(count)
            order_info.goods_price=goods.goods_price
            order_info.goods_total_price=goods.goods_price*int(count)
            order_info.store_id=goods.goods_store#商家卖家，goods.goods_store本身就是一条卖家数据
            order_info.save()
            order_total += order_info.goods_total_price
        order.order_total=order_total
        order.save()
    return render(request,'buyer/pay_order.html',locals())


from Qshop.settings import alipay_public_key_string,alipay_private_key_string
def AlipayViews(request):
    order_number=request.GET.get("order_number")
    order_total=request.GET.get("total")
    # 实例化支付
    alipay = AliPay(
        appid="2016101200667748",
        app_notify_url=None,
        app_private_key_string=alipay_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2"
    )

    # 实例化订单
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_number,  # 订单号
        total_amount=str(order_total),  # 支付金额，是字符串
        subject="生鲜交易",
        return_url="http://127.0.0.1:8000/Buyer/pay_result/",#结果返回的地址
        notify_url="http://127.0.0.1:8000/Buyer/pay_result/"#订单状态发生改变后返回的地址
    )  # 网页支付订单

    # 拼接收款地址=支付宝网管+订单返回参数
    result = "https://openapi.alipaydev.com/gateway.do?" + order_string

    return HttpResponseRedirect(result)
def pay_result(request):
    out_trade_no=request.GET.get("out_trade_no")
    if out_trade_no:
        order=PayOrder.objects.get(order_number=out_trade_no)
        order.orderinfo_set.all().update(order_status=1)
        order.save()
    return render(request,"buyer/alipay.html",locals())

@loginValid
def add_cart(request):
    result={
        "code":200,
        "data":""
    }
    if request.method=="POST":
        id=int(request.POST.get("goods_id"))
        count=int(request.POST.get("count",1))

        goods=Goods.objects.get(id=id)#获取商品信息
        cart=CartGoods()
        cart.goods_name=goods.goods_name
        cart.goods_number=count
        cart.goods_price=goods.goods_price
        cart.goods_picture=goods.picture
        cart.goods_total=goods.goods_price*count
        cart.goods_id=id
        cart.cart_user=request.COOKIES.get("user_id")
        cart.save()
        result["data"]="加入购物车成功"
    else:
        result["code"]=500
        result["data"]="加入购物车失败"
    return JsonResponse(result)

def cart(request):
    user_id=request.COOKIES.get("user_id")
    goods=CartGoods.objects.filter(cart_user=int(user_id)).order_by("-id")
    count=goods.count()
    all_goods=Goods.objects.filter(goods_store=int(user_id))
    for g in goods:
        goods_type=all_goods.get(id=int(g.goods_id))
        goods_count=goods_type.goods_count
    return render(request,'buyer/cart.html',locals())

@loginValid
def user_center_order(request):
    user_id=request.COOKIES.get("user_id")
    user=User.objects.get(id=int(user_id))
    order_list=user.payorder_set.order_by("-order_data")
    return render(request,'buyer/user_center_order.html',locals())


def user_center_site(request):
    return render(request,'buyer/user_center_site.html',locals())



from CeleryTask.tasks import add

def get_task(request):
    num1=request.GET.get("num1",1)
    num2=request.GET.get("num2",2)
    add.delay(int(num1),int(num2))
    return JsonResponse({"data":"success"})