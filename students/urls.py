from django.conf.urls import url
from . import views
from .views import list_view

app_name = 'students'
urlpatterns = [
url(r'^$', views.list_view, name='list_view'),
url(r'^(?P<student_id>[0-9]+)$/', views.detail, name='detail'),
]
