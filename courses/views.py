from django.shortcuts import render
from .models import Course, Lesson


def detail(request, pk):
    courses = Course.objects.filter(id=pk)
    course = courses[0]
    lessons = Lesson.objects.filter(course=pk)
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons, 'pk': pk})
