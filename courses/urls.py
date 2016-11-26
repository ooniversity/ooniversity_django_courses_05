from django.conf.urls import include, url
from courses.views import Course_descr_view
urlpatterns = [
    url(r'^(?P<pk>\d+)/', Course_descr_view.as_view(), name = 'course-description'),
]
