from django.conf.urls import include, url
from django.contrib import admin
from pybursa.views import index, contact, student_detail
from feedbacks import views

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^courses/', include('courses.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^coaches/', include('coaches.urls')),
    url(r'^student_detail/$', student_detail, name='student_detail'),
    url(r'^feedback/', views.FeedbackView.as_view(), name='feedback'),
]
