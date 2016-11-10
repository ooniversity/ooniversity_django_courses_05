from django.conf.urls import url
from quadratic import views
import re

def print2(qqq):
    print(qqq)

urlpatterns = [
    #url(r'^result/(?P<val>\w+)/$', views.result_quadratic, name='quadratic'),
    #url(r'^result/(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/$', views.result_quadratic, name='quadratic'),
    #url(r'^result/?(?P<val>\S[\w-])/$', views.result_quadratic, name='quadratic'),
    #url(r'^result/?a=(?P<a>\w+)&b=(?P<b>\w+)&c=(?P<c>\w+)/$', views.result_quadratic, name='quadratic'),

    #url(r'^(?P<val>.*?)/?$', views.result_quadratic, name='quadratic'),
    url(r'^result/$', views.result_quadratic, name='quadratic'),
    #url(r'^result/??a=(?P<a>\w+)&b=(?P<b>\w+)&c=(?P<c>\w+)/', views.result_quadratic, name='quadratic'),
]

#(.*)\?
