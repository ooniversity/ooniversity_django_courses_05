from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^coaches/', include('coaches.urls')),
    url(r'^feedback/', include('feedbacks.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/$', views.student_detail, name='student_detail')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)),]