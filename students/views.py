from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import StudentModelForm
from .models import Student


def list_view(request):
    course_id = request.GET.get('course_id', None)
    if course_id:
        students = Student.objects.filter(courses__id=course_id)
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def detail(request, pk):
    students = Student.objects.filter(id=pk)
    # courses = Course.objects.filter(courses = pk)
    return render(request, 'students/detail.html', {'students': students, 'pk': pk})


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Student {0} has been successfully added.".format(
                form.cleaned_data['name'] + ' ' + form.cleaned_data['surname']))
            return redirect('../')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
    edit_student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=edit_student)
        if form.is_valid():
            form.save()
            messages.success(request, "Info on the student has been successfully changed.")
            return redirect(reverse('students:edit', args=(pk,)))

    form = StudentModelForm(instance=edit_student)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Info on {0} has been successfully deleted.".format(
                student.name + ' ' + student.surname))
        return redirect(reverse('students:list_view'))
    else:
        form = StudentModelForm(instance=student)
    return render(request, "students/remove.html", {"student": student})
