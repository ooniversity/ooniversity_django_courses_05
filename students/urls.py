from django.conf.urls import include, url
from . import views

app_name = 'students'
urlpatterns = [
    #	url(r'^(?P<curse_id>\d+)/$', views.detail, name='detail'),
    url(r'^$', views.list_view, name='list_view'),
    url(r'^add/$', views.create, name='create'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
    url(r'^(?P<stud_id>\d+)/$', views.detail, name='detail'),
]
