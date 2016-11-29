from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from courses.models import Course

#def index(request):
 #   return render(request, "index.html")

def index(request):
    courses = Course.objects.all()
    return render (request, "index.html", {"courses": courses})

def contact(request):
    return render(request, "contact.html")

def student_list(request):
    return render(request, "student_list.html")

def student_detail(request):
    return render(request, "student_detail.html")


# Create your views here.
