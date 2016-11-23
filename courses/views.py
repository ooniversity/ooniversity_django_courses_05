from django.shortcuts import render
from courses.models import Course, Lesson
from django.http import HttpResponse, HttpResponseNotFound


def detail(request, course_id):
    courses = Course.objects.filter(id=course_id)
    course=courses[0]
    lessons = Lesson.objects.filter(course=course_id)
    return render (request, "courses/detail.html", {"course": course, "course_id":course_id, "lessons": lessons})

