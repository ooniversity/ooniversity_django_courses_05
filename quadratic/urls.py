from quadratic.views import quadratic_results
from django.conf.urls import url, include



app_name = 'quadratic'
urlpatterns = [
    url(r'^results/', quadratic_results, name='results'),
]