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
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')

def hello_c(request):
    return render(request, 'contact.html')

def hello_sd(request):
    return render(request, 'student_detail.html')

def hello_sl(request):
    return render(request, 'student_list.html')


urlpatterns = [
    url(r'^$', hello),
    url(r'index.html', hello),
    url(r'contact.html', hello_c),
    url(r'student_detail.html', hello_sd),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
