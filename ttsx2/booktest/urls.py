from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(\d+)$',views.detail,name='detail'),        #正则表达式非命名组，通过位置参数传递给视图
    url(r'^(?P<p3>\d+)/(?P<p2>\d+)/(?P<p1>\d+)$',views.detail1,name='detail1'),   #正则表达式命名组，通过关键字参数传递给视图，本例中关键字参数为p1,p2,p3
    url(r'^getTest1/$',views.getTest1),
    url(r'^getTest2/$',views.getTest2),
    url(r'^getTest3/$',views.getTest3),
    url(r'^postTest1/$',views.postTest1),
    url(r'^postTest2/$',views.postTest2),
    url(r'^cookieTest/$',views.cookieTest),
    url(r'^redTest1/$',views.redTest1),
    url(r'^redTest2/$',views.redTest2),
    url(r'^session1/$',views.session1),
    url(r'^session2/$',views.session2),
    url(r'^session2_handle/$',views.session2_handle),
    url(r'^session3/$',views.session3)
]
