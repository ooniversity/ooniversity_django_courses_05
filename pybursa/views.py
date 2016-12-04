#from django.http import HttpResponse
from django.shortcuts import render
from courses.models import Course, Lesson

def index(request):
    course_list = Course.objects.all()
    context = {'course_list': course_list}
    return render(request, 'index.html', context)

def contact(request):
	#return render(request, "contact.html") 
	return render(request, 'contact.html')
