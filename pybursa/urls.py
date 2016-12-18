"""pybursa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pybursa import views
from django.shortcuts import render
from django.conf import settings

app_name = 'pybursa'
urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^quadratic/', include('quadratic.urls'), name='quadratic'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
    url(r'^courses/', include('courses.urls')),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    #url(r'^contact/$', views.contact, name='contact'),
    url(r'^coaches/', include('coaches.urls')),
    url(r'^students/', include('students.urls', namespace='students')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)),]