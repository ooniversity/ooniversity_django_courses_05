from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('templates/index.html')
    return HttpResponse(template.render(request))

def contact(request):
    template = loader.get_template('templates/contact.html')
    return HttpResponse(template.render(request))

def student_list(request):
    template = loader.get_template('templates/student_list.html')
    return HttpResponse(template.render(request))

def student_detail(request):
    template = loader.get_template('templates/student_detail.html')
    return HttpResponse(template.render(request))
