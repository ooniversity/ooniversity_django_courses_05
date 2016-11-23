from django.shortcuts import render
from .models import Course, Lesson

def detail(request, pk):
    course = Course.objects.get(id=pk)
    lessons = Lesson.objects.all()
    return render(request, 'courses/detail.html', {'course': course}, {'lessons': lessons})
