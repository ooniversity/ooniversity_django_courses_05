from django.conf.urls import url
from quadratic import views


urlpatterns = [

    url(r'^result/$', views.result_quadratic, name='result_quadratic'),
]

