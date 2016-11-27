from django.conf.urls import url

from .views import detail

app_name = 'coaches'
urlpatterns = [
    #url(r'^$', detail, name='list_view'),
    url(r'^(?P<pk>[0-9]+)/$', detail, name='detail'),
]