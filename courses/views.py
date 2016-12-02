from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from coaches.models import Coach
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages


def detail(request, course_id):
    courses = Course.objects.filter(id = course_id)
    course = courses[0]
    lessons = Lesson.objects.filter(course = course_id)
    i_coach = 0
    i_assist = 0
    coach_qs = Coach.objects.filter(coach_courses = course_id)
    if coach_qs:
        i_coach = 1
        coach = coach_qs[0]
    else:
        coach = False
    assistant_qs = Coach.objects.filter(assistant_courses = course_id)
    if assistant_qs:
        i_assist = 1
        assistant = assistant_qs[0]
    else:
        assistant = False
    return render (request, "courses/detail.html", {"course": course, "course_id":course_id, 
                             "lessons": lessons, "coach": coach, "assistant": assistant, 
                             "i_coach": i_coach, "i_assist": i_assist}, )


def add(request):
    model_form = CourseModelForm()
    if request.method == "POST":
       form = CourseModelForm(request.POST)
       if form.is_valid():
           instance = form.save()
           messages.success(request, "Course {0} has been successfully added.".format(form.cleaned_data['name']))
           return redirect('../../')
    else:
        form = CourseModelForm()
    return render(request, "courses/add.html", {'form': form})


def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
       form = CourseModelForm(request.POST, instance=course)
       if form.is_valid():
           course = form.save()
           messages.success(request, "The changes have been saved.")
           return redirect('/courses/{0}/'.format(course_id))
    else:
        form = CourseModelForm(instance=course)
    return render(request, "courses/edit.html", {'form': form})

def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
       course.delete()
       messages.success(request, "Course {0} has been deleted.".format(course.name))
       return redirect('/')
    else:
        form = CourseModelForm(instance=course)
    return render(request, "courses/remove.html", {"course": course})

def add_lesson(request, course_id):
    course = Course.objects.get(id=course_id)
    model_form = LessonModelForm(initial={"course": course.name})
    if request.method == "POST":
       form = LessonModelForm(request.POST)
       if form.is_valid():
           instance = form.save()
           messages.success(request, "Lesson {0} has been successfully added.".format(form.cleaned_data['subject']))
           return redirect('/courses/{0}/'.format(course_id))
    else:
        form = LessonModelForm(initial={"course": course.name})
    return render(request, "courses/add_lesson.html", {'form': form})



