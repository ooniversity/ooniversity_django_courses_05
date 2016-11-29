from django.shortcuts import render
from students.models import Student
from courses.models import Course
from django.http import HttpResponse, HttpResponseNotFound

def list_view(request):
    if request.GET.get('course_id')==None:
        students = Student.objects.all()
    else:
        course_id = request.GET.get('course_id')
        students_course = Student.objects.filter(courses__id=course_id)
        students = students_course[0:]
    return render (request, "students/list.html", {"students_list": students,} )

def detail(request, student_id):
    student = Student.objects.filter(id=student_id)
    return render (request, "students/detail.html", {"student": student,})
