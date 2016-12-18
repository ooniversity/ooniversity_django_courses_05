from django.conf.urls import include, url
from . import views

#from django.contrib.flatpages import views

app_name = 'students'
urlpatterns = [
    #	url(r'^(?P<curse_id>\d+)/$', views.detail, name='detail'),
    url(r'^$', views.StudentListView.as_view(), name='list_view'),
    url(r'^add/$', views.StudentCreateView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', views.UpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove'),
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
    #url(r'^?page=(?P<page_number>\d+)$', views.list_view, name='list_view'),
]
