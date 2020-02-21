from django.conf.urls import include,url
from . import views

urlpatterns=[
    url(r'^$',views.index), #当匹配成功后，调用views.index视图
    url(r'^(\d+)$',views.detail)  #(\d+)即取id值
]