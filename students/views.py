from .models import Student
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentModelForm

def list_view (request):
    try:
        context = Student.objects.filter(courses=int(request.GET['course_id']))
    except:
        context = Student.objects.all()
    return render(request, 'students/list.html', {'students_list': context})

def detail(request, student_id):
    context = Student.objects.get(id=int(student_id))
    return render(request, 'students/detail.html', {'student': context})

def create(request):
    if request.POST:
        model_form = StudentModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, 'Student {0} {1} has been successfully added'.format(
                                                            model_form.cleaned_data['name'],
                                                            model_form.cleaned_data['surname']))
            return redirect('/students/')
    else:
        model_form = StudentModelForm()
    return render(request, "students/add.html", {"model": model_form})

def edit(request, student_id):
    student = Student.objects.get(id=int(student_id))
    if request.POST:
        model_form = StudentModelForm(request.POST, instance=student)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect('/students/edit/{0}/'.format(student_id))
    else:
        model_form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {"model": model_form})

def remove(request, student_id):
    student = Student.objects.get(id=int(student_id))
    if request.POST:
        student.delete()
        messages.success(request, 'Info on {0} {1} has been successfully deleted.'.format(student.name, student.surname))
        return redirect('/students/')
    else:
        return render(request, 'students/remove.html', {"model": student})