from Qshop.urls import *
from Buyer.views import *
urlpatterns = [
    path('login/',login),#买家登录校验页面url
    path('register/',register),#买家注册页面url
    path('logout/',logout),#买家登出功能
    path('index/',index),#买家主页面
    path('goods_list/',goods_list),
    re_path('goods_details/(?P<id>\d+)/',goods_details),#ajax功能
    path('user_center_info/',user_center_info),
    #支付功能
    path('pay_order/',pay_order),
    path('pay_order_more/',pay_order_more),
    path('alipay/',AlipayViews),
    path('pay_result/',pay_result),
    path('add_cart/',add_cart),
    path('cart/',cart),
    path('user_center_order/',user_center_order),
    path('user_center_site/',user_center_site),
    path('gt/',get_task)


]