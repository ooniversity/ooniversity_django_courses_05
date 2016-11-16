from django.conf.urls import url

from . import views

app_name = 'quadratic'
urlpatterns = [
    url(r'^results/$', views.quadratic_results, name='quadratic_results'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
