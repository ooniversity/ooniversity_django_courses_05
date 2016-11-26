#import django.shortcuts, math
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from .models import Course, Lesson
# -*- coding: utf-8 -*-

# Create your views here.
def main(request):
    course_list = Course.objects.all()
    context = {'course_list': course_list}
    return render(request, 'main.html', context)

def detail(request, curse_id):
    course_name = Course.objects.get(id = curse_id)
    lesson_list = Lesson.objects.filter(course_id = curse_id)
    return render(request, 'detail.html', {'lesson_list': lesson_list,
                                           'course_name': course_name,
                                           'curse_id': curse_id})

#/root/789/ooniversity_django_courses_05/courses/templates/courses/
#request,