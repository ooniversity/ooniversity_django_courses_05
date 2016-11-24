from django.shortcuts import render, get_object_or_404
from courses.models import Course
from students.models import Student

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses' : courses})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students' : students})

def student_detail(request):
    return render(request, 'student_detail.html')
