#import django.shortcuts, math
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, redirect
from .models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
#from pybursa.utils import detail_view
# -*- coding: utf-8 -*-

#def detail(request, pk):
#    return detail_view(request, pk, Course)

# Create your views here.
def detail(request, curse_id):
    course_name = Course.objects.get(id = curse_id)
    lesson_list = Lesson.objects.filter(course_id = curse_id)
    return render(request, 'courses/detail.html', {'lesson_list': lesson_list,
                                           'course_name': course_name,
                                           'curse_id': curse_id})

#def course_apply(request):
##if request.method == "POST":
#form = ModelCourseApplyForm(request.POST)
#if form.is_valid():
#instance = form.save()
#messages.success(request, "Saved!!!!")
#return redirect ("/apply/")
#else:
#form = ModelCourseApplyForm(initial={'package':'gold', 'news_subscribe':True})
#return render(request, 'apply.html', {'form': form})

def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            data = form.cleaned_data
            name = data['name']
            messages.success(request, "Course %s has been successfully added." % name)
            return redirect("/")
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})

def edit(request, pk):
    course = Course.objects.get(id = pk)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        print(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, "The changes have been saved.")
            return redirect("/courses/edit/{0}/'.format(course_id)")
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})

def remove(request, pk):
    course = Course.objects.get(id = pk)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course %s has been deleted." % course.name)
        return redirect("/")
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/remove.html', {'course': course})

def add_lesson(request, z):
    course = Course.objects.get(id=z)
    lesson = Lesson.objects.filter( id = z )
    if request.method == "POST":
        form = LessonModelForm(request.POST, initial = {'course': 'lesson.course'})
        if form.is_valid():
            instance = form.save()
            data = form.cleaned_data
            name = data['name']
            messages.success(request, "Lesson %s has been successfully added." %name)
            return redirect("/courses/{{ curse.id }}/")
    else:
        form = LessonModelForm(initial = {'course': 'lesson.course'})
    return render(request, 'courses/add_lesson.html', {'form': form})

