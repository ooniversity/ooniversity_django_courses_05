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
        list_students = Student.objects.filter(courses = course_id)
        course_name = Course.objects.all()
    return render(request, 'students/templates/students/list_view.html', {'list_students': list_students,
                                            'course_name': course_name})

def detail(request, stud_id):
    student_full = Student.objects.get(id=stud_id)
    course_name = Course.objects.filter(student = student_full.id)
    print(course_name)
    return render(request, 'students/templates/students/detail.html', {'stud_id': stud_id,
                                                                       'student_full': student_full,
                                                                       'course_name': course_name})

# Create your views here.
