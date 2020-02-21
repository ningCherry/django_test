from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^pro/$',views.pro),
    url(r'^city(\d+)/$',views.city),
    url(r'^content/$',views.content),
    url(r'^content_handle/$',views.content_handle),
    url(r'^cache1/$',views.cache1),
    url(r'^mysearch/$',views.mysearch),
    url(r'^celeryTest/$',views.celeryTest),
]