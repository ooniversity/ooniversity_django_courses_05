from django.conf.urls import patterns, url

from quadratic import views


urlpatterns = patterns('',
    #url(r'^results/$', views.quadratic_results, name='results'),
	#url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^results/$', views.QuadraticResultsView.as_view(), name='results'),
)