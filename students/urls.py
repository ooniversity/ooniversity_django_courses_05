from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^remove/(?P<pk>\d+)/', views.remove, name='remove'),
    url(r'^edit/(?P<pk>\d+)/', views.edit, name='edit'),
    url(r'^add/', views.create, name='add'),
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
]
