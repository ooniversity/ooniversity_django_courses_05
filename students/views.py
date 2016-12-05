from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from .models import Student, Course
from students.forms import StudentModelForm
from django.contrib import messages
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

def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            data = form.cleaned_data
            name = data['name']
            surname = data['surname']
            messages.success(request, "Student %s %s has been successfully added." % (name,surname))
            return redirect("/students/")
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, pk):
    student = Student.objects.get(id = pk)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        print(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Info on the student has been successfully changed.")
            return redirect("/students/")
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, pk):
    student = Student.objects.get(id = pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Info on %s has been successfully deleted." % student.full_name)
        return redirect("/students/")
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/remove.html', {'student': student})
