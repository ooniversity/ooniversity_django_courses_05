from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course
from .forms import CourseModelForm, LessonModelForm


def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'templates/courses/detail.html', {'course': course})

def create(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Course {} has been successfully added.'.format(course.name))
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'templates/courses/add.html', {'form': form})

def edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', course.id)
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'templates/courses/edit.html', {'form': form})

def remove(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        messages.success(request, 'Course {} has been deleted.'.format(course.name))
        return redirect('index')
    return render(request, 'templates/courses/remove.html', {'course': course})

def add_lesson(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Lesson {} has been successfully added.'.format(lesson.subject))
            return redirect('courses:detail', lesson.course_id)
    else:
        form = LessonModelForm(initial={'course': course})
    return render(request, 'templates/courses/add_lesson.html', {'form': form})

