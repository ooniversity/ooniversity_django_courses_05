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
    #url(r'^index/$', views.index, name='index'),
    #url(r'^contact/$', views.contact, name='contact'),
    #url(r'^student_list/$', views.student_list, name='student_list'),
    #url(r'^student_detail/$', views.student_detail, name='student_detail')
]
