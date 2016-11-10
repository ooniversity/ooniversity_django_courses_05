from django.conf.urls import url
from quadratic import views
import re

urlpatterns = [
    #url(r'^result/(?P<val>\w+)/$', views.result_quadratic, name='quadratic'),
    #url(r'^result/(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/$', views.result_quadratic, name='quadratic'),
    #url(r'^result/?(?P<val>\S[\w-])/$', views.result_quadratic, name='quadratic'),
    url(r'^result/?a=(?P<a>\w+)&b=(?P<b>\w+)&c=(?P<c>\w+)/$', views.result_quadratic, name='quadratic'),
]

#(.*)\?
