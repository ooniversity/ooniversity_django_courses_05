from django.shortcuts import render, get_object_or_404
from courses.models import Course


def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'templates/courses/detail.html', {'course': course})

