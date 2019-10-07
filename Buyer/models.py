from django.db import models
from Seller.models import User

#订单建模
class PayOrder(models.Model):
    """
    订单表
    订单状态
        0 未支付
        1 已支付
        2 待收货
        3/4 已签收/拒收
    """
    order_number=models.CharField(max_length=32)
    order_data=models.DateTimeField(auto_now=True)
    order_total=models.FloatField(blank=True,null=True)
    order_user=models.ForeignKey(to=User,on_delete=models.CASCADE)


#订单详情表
class OrderInfo(models.Model):
    order_id=models.ForeignKey(to=PayOrder,on_delete=models.CASCADE)
    goods_id=models.IntegerField()
    goods_picture=models.CharField(max_length=32)
    goods_name=models.CharField(max_length=32)
    goods_count=models.IntegerField()
    goods_price=models.FloatField()
    goods_total_price=models.FloatField()

    order_status=models.IntegerField(default=0)

    store_id=models.ForeignKey(to=User,on_delete=models.CASCADE)

#购物车页
class CartGoods(models.Model):
    """
    商品名称
    商品数量（购买的数量）
    商品价格
    商品图片
    商品总价（单类商品总价）
    商品id
    用户
    """
    goods_name = models.CharField(max_length=32)
    goods_number=models.IntegerField()
    goods_price = models.FloatField()
    goods_picture=models.CharField(max_length=32)
    goods_total= models.FloatField()
    goods_id = models.IntegerField()
    cart_user=models.IntegerField()


# Create your models here.
