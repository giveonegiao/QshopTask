from Qshop.urls import path,re_path
from Seller.views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('register/',cache_page(60*15)(register)),#卖家注册页面url
    path('login/',login),#卖家登录校验页面url
    path('logout/',logout),#卖家登出url
    path('index/',index),#卖家主页面url


    re_path('goods_list/(?P<status>[01])/(?P<page>\d+)/',goods_list),
    re_path('goods_status/(?P<state>\w+)/(?P<id>\d+)/',goods_status),
    path('person_info/',person_info),
    path('goods_add/',goods_add),
    path('send_login_code/',send_login_code),
    re_path(r'order_list/(?P<status>\d{1})',order_list),
    path("change_order/",change_order),

]
