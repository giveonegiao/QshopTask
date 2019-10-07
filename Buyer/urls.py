from Qshop.urls import *
from Buyer.views import *
urlpatterns = [
    path('login/',login),
    path('register/',register),
    path('logout/',logout),
    path('index/',index),
    path('goods_list/',goods_list),
    re_path('goods_details/(?P<id>\d+)/',goods_details),
    path('user_center_info/',user_center_info),
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