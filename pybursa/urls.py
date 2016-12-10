from pybursa import views
from django.conf.urls import include, url
from django.contrib import admin
from feedbacks.views import FeedbackView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'courses/', include('courses.urls', namespace="courses")),
    url(r'students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'feedback/$', FeedbackView.as_view(), name='feedback'),
]
