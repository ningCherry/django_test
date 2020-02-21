from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^myexception$',views.myExc),
    url(r'^uploadPic$',views.uploadPic),
    url(r'^uploadHandle$',views.uploadHandle),
    url(r'^herolist/(\d*)$',views.herolist),  #\d*，正则可以不输入数字。\d+必须输入数字
    url(r'^area$',views.area),  #\d*，正则可以不输入数字。\d+必须输入数字
    url(r'^area/(\d+)$',views.area2),  #\d*，正则可以不输入数字。\d+必须输入数字
]