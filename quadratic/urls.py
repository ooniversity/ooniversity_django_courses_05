from django.conf.urls import url

from .views import quadratic_results

app_name = 'quadratic'
urlpatterns = [
    url(r'^results/(?P<a>[0-9])&(?P<b>[0-9])&(?P<c>[0-9])/$', quadratic_results, name = 'results'),

]