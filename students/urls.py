from django.conf.urls import url
from . import views
from .views import list_view, add, edit, remove

app_name = 'students'
urlpatterns = [
url(r'^$', views.list_view, name='list_view'),
url(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),
url(r'^add/$', add, name='add'),
url(r'^edit/(?P<student_id>[0-9]+)/$', edit, name='edit'),
url(r'^remove/(?P<student_id>[0-9]+)/$', remove, name='remove'),
]
