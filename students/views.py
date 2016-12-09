from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from courses.models import Course
from .forms import StudentModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

class StudentDetailView(DetailView):
    model = Student
    #template_name = 'student/detail.html'

class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses=course_id)
        return qs

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')


    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, 'Student %s %s was added' %
                        (form.instance.name, form.instance.surname))
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context   

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    #template_name = 'students/edit.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, 'Info changed')
        return result

    def get_success_url(self):
        return reverse('students:edit', args=(self.object.pk,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Info on %s %s has been successfully deleted.' %
                         (self.object.name, self.object.surname))
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context