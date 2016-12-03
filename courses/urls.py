from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf.urls.static import static

app_name = 'courses'

urlpatterns = [
    #url(r'^polls/', include('polls.urls')),
    #url(r'^quadratic/', include('quadratic.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<course_id>[\d]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<course_id>[\d]+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<course_id>[\d]+)/$', views.remove, name='remove'),
    url(r'^(?P<course_id>[\d]+)/add_lesson$', views.add_lesson, name='add_lesson'),

]
