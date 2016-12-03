from django.shortcuts import render, get_object_or_404, redirect
from students.models import Student
from django.contrib import messages
from .forms import StudentModelForm


def list_view(request):
    course_id = request.GET.get('course_id', None)
    if course_id:
        students = Student.objects.filter(courses__id=course_id)
    else:
        students = Student.objects.all()
    return render(request, 'templates/students/list.html', {'students': students})


def detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'templates/students/detail.html', {'student': student})

def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Student {} {} has been successfully added.'.format(student.name, student.surname))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'templates/students/add.html', {'form': form})

def edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Changes has been saved')
            return redirect('students:edit', student.id)
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'templates/students/edit.html', {'form': form})


def remove(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, 'Student {} {} has been deleted.'.format(student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'templates/students/remove.html', {'student': student})

