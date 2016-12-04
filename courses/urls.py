from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
    url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^add/$', views.create, name='add'),
]

