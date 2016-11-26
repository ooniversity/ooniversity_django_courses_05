from django.conf.urls import include, url
from . import views

app_name = 'students'
urlpatterns = [
    #	url(r'^(?P<curse_id>\d+)/$', views.detail, name='detail'),
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<stud_id>\d+)/$', views.detail, name='detail'),
]
