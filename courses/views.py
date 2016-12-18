#import django.shortcuts, math
from django.shortcuts import render, redirect
#from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, redirect
from .models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("courses")
#from pybursa.utils import detail_view
# -*- coding: utf-8 -*-

#def detail(request, pk):
#    return detail_view(request, pk, Course)


# Create your views here.
class CourseDetailView(DetailView):
    model = Course
    logger.debug("Courses detail view has been debugged!")
    logger.info("Logger of courses detail view informs you!")
    logger.warning("Logger of courses detail view warns you!")
    logger.error("Courses detail view went wrong!")
    fields = '__all__'
    context_object_name = 'course_name'
    template_name = 'courses/detail.html'


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    form_class = CourseModelForm
    template_name = 'courses/add.html'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        data = form.cleaned_data
        messages.success(self.request, "Course %s has been successfully added." % data['name'])
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/edit.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        data = form.instance
        messages.success(self.request, 'The changes have been saved.')
        self.success_url = reverse_lazy('courses:edit', args=(data.id,))
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        messages.success(self.request, "Info on %s has been deleted." % course.name)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)


def add_lesson(request, z):
    course = Course.objects.get(id=z)
    lesson = Lesson.objects.filter( id = z )
    if request.method == "POST":
        form = LessonModelForm(request.POST, initial = {'course': 'lesson.course'})
        if form.is_valid():
            instance = form.save()
            data = form.cleaned_data
            subject = data['subject']
            messages.success(request, "Lesson %s has been successfully added." %subject)
            return redirect("/courses/{0}/".format(course.id))
    else:
        form = LessonModelForm(initial = {'course': 'lesson.course'})
    return render(request, 'courses/add_lesson.html', {'form': form})

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

