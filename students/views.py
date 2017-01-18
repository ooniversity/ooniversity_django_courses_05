from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic import DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import StudentModelForm
from .models import Student

import logging

logger = logging.getLogger(__name__)


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.debug("Students detail view has been debugged!")
        logger.info("Logger of students detail view informs you!")
        logger.warning("Logger of students detail view warns you!")
        logger.error("Students detail view went wrong!")
        return context


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        s = super().form_valid(form)
        messages.success(self.request, "Student {0} has been successfully added.".format(
            self.object.name + ' ' + self.object.surname))
        return s

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        context['button'] = 'Создать'
        return context


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        s = super().form_valid(form)
        messages.success(self.request, "Info on the student has been successfully changed.")
        return s

    def get_success_url(self):
        super().get_success_url()
        pk = self.kwargs['pk']
        return reverse('students:edit', args=(pk,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        context['button'] = 'Изменить'
        return context


class StudentDeleteView(DeleteView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        d = super().delete(request, *args, **kwargs)
        messages.success(request, "Info on {0} has been successfully deleted.".format(
            self.object.name + ' ' + self.object.surname))
        return d

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context
