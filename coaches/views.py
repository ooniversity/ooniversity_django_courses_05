from django.shortcuts import render
from .models import Coach
from courses.models import Course


def detail(request, pk):
    coaches = Coach.objects.filter(id=pk)
    courses_teacher = Course.objects.filter(coach_id=pk)
    courses_asistent = Course.objects.filter(assistant_id=pk)
    return render(request, 'coaches/detail.html', {'coaches': coaches, 'courses_teacher': courses_teacher,'courses_asistent': courses_asistent, 'pk': pk})

