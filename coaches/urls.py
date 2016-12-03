from django.conf.urls import url
from . import views


app_name = 'coaches'

urlpatterns = [
    url(r'^(?P<coach_id>[0-9]+)/$', views.detail, name='detail'),
]