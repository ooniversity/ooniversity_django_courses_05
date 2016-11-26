from django.conf.urls import url
from courses.views import detail

app_name = 'courses'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', detail, name='detail'),
]
