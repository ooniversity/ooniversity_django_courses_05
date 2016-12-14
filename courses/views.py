from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from coaches.models import Coach
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

import logging
logger = logging.getLogger(__name__)

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        logger.debug("Courses detail view has been debugged!")
        logger.info("Logger of courses detail view informs you!")        
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['lessons'] = Lesson.objects.filter(course__id=pk)
        return context


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('index')
    template_name = 'courses/add.html'
    context_object_name = 'course'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Course {0} has been successfully added.".format(form.cleaned_data['name']))
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation' 
        return context


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('index')
    template_name = 'courses/edit.html'
    context_object_name = 'course'
    
    def get_success_url(self):
        super().get_success_url()
        pk = self.kwargs['pk']
        return reverse('courses:edit', args=(pk,))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "The changes have been saved.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update' 
        return context


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'
    context_object_name = 'course'
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(self.request, "Course {0} has been deleted.".format(
            self.object.name))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion' 
        return context


class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonModelForm
    success_url = reverse_lazy('index')
    template_name = 'courses/add_lesson.html'
    context_object_name = 'lessons'
    
    def get_success_url(self):
        super().get_success_url()
        pk = self.kwargs['pk']
        return reverse('courses:detail', args=(pk,))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Lesson {0} has been successfully added.".format(form.cleaned_data['subject']))
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lesson creation' 
        return context







