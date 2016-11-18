from django.shortcuts import render
from students.models import Student


def students_list(request):

    student_list = Student.objects.all()
    context = {'students': student_list}
    return render(request, 'students_list.html', context)