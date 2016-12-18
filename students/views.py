from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from .models import Student, Course
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pybursa.utils import detail_view
from django.urls import reverse_lazy
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("students")

class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id = course_id)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Студентики'
        return context

#def list_view(request):
 #   course_id = request.GET.get('course_id')
  #  if course_id is None:
   #     list_students = Student.objects.all()
       # import pdb;pdb.set_trace()
       # paginator = Paginator(list_students, 2)
       # course_name = Course.objects.all()
        #if request.method =="GET":
         #   page_number = request.GET.get('page', 1)
       #     page_number = int(page_number)
        #    page = paginator.page(int(page_number))
         #   try:
          #      page = paginator.page(page)
           # except PageNotAnInteger:
                # If page is not an integer, deliver first page.
            #    page = paginator.page(1)
            #except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
             #   page = paginator.page(paginator.num_pages)
    #else:
     #   list_students = Student.objects.filter(courses__id = int(course_id))
       # paginator = Paginator(list_students, 2)
        #page_number = request.GET.get('page', 1)
        #page = paginator.page(page_number)
        #try:
         #   page = paginator.page(page)
        #except PageNotAnInteger:
            # If page is not an integer, deliver first page.
         #   page = paginator.page(1)

#        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
 #           page = paginator.page(paginator.num_pages)
      #  return render(request, 'students/list.html', {'list_students': list_students})

#def detail(request, pk):
 #   logger.debug("Students detail view has been debugged!")
  #  logger.info("Logger of students detail view informs you!")
   # logger.warning("Logger of students detail view warns you!")
   # logger.error("Students detail view went wrong!")
   # student_full = get_object_or_404(Student, id=int(pk))
    #student_full = Student.objects.get(id=int(stud_id))
   # return render(request, 'students/detail.html', {'student_full': student_full})

class StudentDetailView(DetailView):
    model = Student
    logger.debug("Students detail view has been debugged!")
    logger.info("Logger of students detail view informs you!")
    logger.warning("Logger of students detail view warns you!")
    logger.error("Students detail view went wrong!")
    template_name = 'students/detail.html'

class SomeFormView(FormView):
        form_class = StudentModelForm
        template_name = 'students/edit.html'
        success_url = '/students/'

        def form_invalid(self, form):
            student = form.save()
            messages.success(self.request, "Info on the student has been successfully changed.")


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm
    template_name = 'students/add.html'

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        data = form.cleaned_data
        messages.success(self.request, "Student %s %s has been successfully added." % (data['name'], data['surname']))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'students/edit.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        data = form.instance
        messages.success(self.request, 'Info on the student has been successfully changed.')
        self.success_url = reverse_lazy('students:list_view')
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    #form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    template_name = 'students/remove.html'

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, "Info on %s has been successfully deleted." % student.full_name)
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)