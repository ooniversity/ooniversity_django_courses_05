from django.shortcuts import render
from .models import Course, Lesson
from coaches.models import Coach


def detail(request, pk):
    courses = Course.objects.filter(id=pk)
    course = courses[0]
    coaches = Coach.objects.filter(coach_courses=pk)
    assistants = Coach.objects.filter(assistant_courses=pk)
    lessons = Lesson.objects.filter(course=pk)
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons, 'pk': pk, 'coaches': coaches, 'assistants': assistants})
