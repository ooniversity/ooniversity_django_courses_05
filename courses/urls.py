from django.conf.urls import include, url
from . import views

app_name = 'courses'
urlpatterns = [
	url(r'^(?P<curse_id>\d+)/$', views.detail, name='detail'),
]

#

