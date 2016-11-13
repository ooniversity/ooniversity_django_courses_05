from django.conf.urls import url
from . import views
from .views import quadratic_results

app_name = 'quadratic'
urlpatterns = [
url(r'^results/$', quadratic_results),
]
