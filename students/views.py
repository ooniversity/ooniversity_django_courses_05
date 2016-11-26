from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from students.models import Student

class List_View(ListView):

    model = Student
    template_name = "../templates/students/list_view.html"

    def get_queryset(self):
        return Student.objects.all()

class StudentDescr(DetailView):
    model = Student
    template_name = "../templates/students/details.html"

