from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach
from django.http import HttpResponse, HttpResponseNotFound




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

