from django.shortcuts import render
from .models import Student
from courses.models import Course

def list_view (request):
    course_id = request.GET.get('course_id', None)
    if course_id:
        students = Student.objects.filter(courses__id = course_id)
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def detail (request, pk):
    students = Student.objects.filter(id = pk)
    # courses = Course.objects.filter(courses = pk)
    return render(request, 'students/detail.html', {'students': students, 'pk': pk})
