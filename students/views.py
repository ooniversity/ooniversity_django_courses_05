from .models import Student
from django.shortcuts import render

def list_view (request):
    try:
        context = Student.objects.filter(courses=int(request.GET['course_id']))
    except:
        context = Student.objects.all()
    return render(request, 'students/list.html', {'students_list': context})

def detail(request, pk):
    context = Student.objects.get(id=int(pk))
    return render(request, 'students/detail.html', {'student': context})