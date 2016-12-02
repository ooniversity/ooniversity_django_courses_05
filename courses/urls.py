from django.conf.urls import url
from . import views
from .views import detail, add, edit, remove, add_lesson

app_name = 'courses'
urlpatterns = [
url(r'^(?P<course_id>[0-9]+)/$', views.detail, name='detail'),
url(r'^add/$', add, name='add'),
url(r'^edit/(?P<course_id>[0-9]+)/$', edit, name='edit'),
url(r'^remove/(?P<course_id>[0-9]+)/$', remove, name='remove'),
url(r'^(?P<course_id>[0-9]+)/add_lesson$', add_lesson, name='add_lesson'),
]
