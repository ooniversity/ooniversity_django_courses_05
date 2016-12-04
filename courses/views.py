from django.shortcuts import render, redirect
from .models import Course, Lesson
from .forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def detail(request, pk):
    context = Course.objects.get(id=int(pk))
    return render(request, 'courses/detail.html', {'course': context})

def add(request):
    if request.method == 'POST':
        model_form = CourseModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, "Course {0} has been successfully added.".format(model_form.cleaned_data['name']))
            return redirect('/')
    else:
        model_form = CourseModelForm()
    return render(request, 'courses/add.html', {'model': model_form})

def add_lesson(request, pk):
    if request.method == 'POST':
        model_form = LessonModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, 'Lesson {0} has been successfully added'.format(model_form.cleaned_data['subject']))
            return redirect('/courses/{0}/'.format(pk))
    else:
        model_form = LessonModelForm(initial={'course': pk})
    return render(request, 'courses/add_lesson.html', {'model': model_form})


def edit(request, pk):
    course = Course.objects.get(id=int(pk))
    if request.method == 'POST':
        model_form = CourseModelForm(request.POST, instance=course)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('/courses/edit/{0}/'.format(pk))
    else:
        model_form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'model': model_form})

def remove(request, pk):
    course = Course.objects.get(id=int(pk))
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course {0} has been deleted.'.format(course.name))
        return redirect('/')
    else:
        model_form = CourseModelForm(instance=course)
    return render(request, 'courses/remove.html', {'model': model_form})
