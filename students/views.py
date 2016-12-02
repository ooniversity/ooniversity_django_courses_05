from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from django.http import HttpResponse, HttpResponseNotFound
from .forms import StudentModelForm
from django.contrib import messages

def list_view(request):
    if request.GET.get('course_id')==None:
        students = Student.objects.all()
    else:
        course_id = request.GET.get('course_id')
        students_course = Student.objects.filter(courses__id=course_id)
        students = students_course[0:]
    return render (request, "students/list.html", {"students_list": students,} )

def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render (request, "students/detail.html", {"student": student,})

def create(request):
    model_form = StudentModelForm()
    if request.method == "POST":
       form = StudentModelForm(request.POST)
       if form.is_valid():
           instance = form.save()
#           data = form.cleaned_data
           messages.success(request, "Student {0} has been successfully added.".format(form.cleaned_data['name'] + ' ' + form.cleaned_data['surname']))
           return redirect('../')
    else:
        form = StudentModelForm()
    return render(request, "students/add.html", {'form': form})


def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
       form = StudentModelForm(request.POST, instance=student)
       if form.is_valid():
           student = form.save()
           messages.success(request, "Info on the student has been successfully changed.")
           return redirect('../../')
    else:
        form = StudentModelForm(instance=student)
    return render(request, "students/edit.html", {'form': form})

def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
       student.delete()
       messages.success(request, "Info on {0} has been successfully deleted.".format(student.name))
       return redirect('../../')
    else:
        form = StudentModelForm(instance=student)
    return render(request, "students/remove.html", {"student": student})

# Create your views here.
