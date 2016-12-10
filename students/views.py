from django.shortcuts import render, get_object_or_404, redirect
from students.models import Student
from django.contrib import messages
from .forms import StudentModelForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(self.request, 'Student %s %s has been added successfully.' % (data['name'], data['surname']))
        return super(StudentCreateView, self).form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Update info"
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Student information has been changed successfully.')
        return super(StudentUpdateView, self).form_valid(form)

class StudentDeleteView(DeleteView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, 'Information on %s %s has been deleted successfully.' % (student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)

