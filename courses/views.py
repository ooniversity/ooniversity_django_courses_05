from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Lesson
from students.models import Student


def detail(request, course_id):
    qs = Course.objects.get(id=course_id)
    leson = Lesson.objects.filter(course=qs)
    return render(request, 'courses/detail.html', {'course': qs, 'lessons': leson})
# Create your views here.
