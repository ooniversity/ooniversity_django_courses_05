#from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader


def index(request):
    return render(request, 'templates/index.html')

def contact(request):
    return render(request, 'templates/contact.html')

def student_list(request):
    return render(request, 'templates/student_list.html')

def student_detail(request):
    return render(request, 'templates/student_detail.html')
