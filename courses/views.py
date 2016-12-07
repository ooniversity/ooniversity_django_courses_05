from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from courses.forms import CourseModelForm, LessonModelForm
from .models import Course, Lesson
from coaches.models import Coach


def detail(request, pk):
    course = Course.objects.filter(id=pk)
    coaches = Coach.objects.filter(coach_courses=pk)
    assistants = Coach.objects.filter(assistant_courses=pk)
    lessons = Lesson.objects.filter(course=pk)
    return render(request, 'courses/detail.html',
                  {'course': course, 'lessons': lessons, 'pk': pk, 'coaches': coaches, 'assistants': assistants})


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course {0} has been successfully added.".format(
                form.cleaned_data['name']))
            return redirect('/')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})


def edit(request, pk):
    edit_course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=edit_course)
        if form.is_valid():
            form.save()
            messages.success(request, "The changes have been saved.")
            return redirect(reverse('courses:edit', args=(pk,)))

    form = CourseModelForm(instance=edit_course)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course {0} has been deleted.".format(
            course.name))
        return redirect(reverse('index'))
    else:
        form = CourseModelForm(instance=course)
    return render(request, "courses/remove.html", {"course": course})


def add_lesson(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, "Lesson {0} has been successfully added.".format(
                lesson.subject))
            return redirect(reverse('courses:detail', args=(lesson.course.id,)))
    else:
        form = LessonModelForm(initial={"course": course.id})
    return render(request, 'courses/add_lesson.html', {'form': form})
