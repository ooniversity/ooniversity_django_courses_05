#from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from courses.models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'templates/index.html', {'courses': courses})
#    template = loader.get_template('templates/index.html')
#    return HttpResponse(template.render(request))

def contact(request):
    return render(request, 'templates/contact.html')
#    template = loader.get_template('templates/contact.html')
#    return HttpResponse(template.render(request))

#def student_list(request):
#    template = loader.get_template('templates/student_list.html')
#    return HttpResponse(template.render(request))

#def student_detail(request):
#    template = loader.get_template('templates/student_detail.html')
#    return HttpResponse(template.render(request))
