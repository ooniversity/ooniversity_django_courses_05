from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from .models import Student, Course
# -*- coding: utf-8 -*-

def list_view(request):
    course_id = request.GET.get('course_id')
    if course_id is None:
        list_students = Student.objects.all()
        course_name = Course.objects.all()
    else:
        course_id = int(course_id)
        list_students = Student.objects.filter(courses__id = course_id)
        #student = list_students[0:]
        #course_name = Course.objects.all()
    return render(request, 'students/list.html', {'list_students': list_students})

def detail(request, stud_id):
    student_full = Student.objects.get(id=int(stud_id))
    #course_name = Course.objects.filter(student = student_full.id)
    #course_name = Course.objects.filter(student=student_full.name)
    return render(request, 'students/detail.html', {'student_full': student_full})

# Create your views here.
