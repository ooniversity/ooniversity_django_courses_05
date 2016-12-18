from django.conf.urls import include, url
from . import views

app_name = 'courses'
urlpatterns = [
	url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),
	url(r'^add/$', views.add, name='add'),
	url(r'^edit/(?P<curse_id>\d+)/$', views.edit, name='edit'),
	url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
	url(r'^(?P<z>\d+)/add_lesson$', views.add_lesson, name='add_lesson'),

]
