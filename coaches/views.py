from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
from django.http import HttpResponse, HttpResponseNotFound

def detail(request, coach_id):
    coach = Coach.objects.filter(id = coach_id)

    coach_course_qs = Course.objects.filter(coach_id = coach_id)
    coach_course = coach_course_qs[0:]
       
    assistant_course_qs = Course.objects.filter(assistant_id = coach_id)
    assistant_course = assistant_course_qs[0:]

    return render (request, "coaches/detail.html", {"coach": coach, "coach_course": coach_course, "assistant_course": assistant_course })
