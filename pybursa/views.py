from django.http import HttpResponse, response
from django.shortcuts import render
from courses.models import Course
from django.views.generic.base import TemplateView
from django.views.decorators.cache import cache_page

def index(request):
	courses = Course.objects.all()
	return render(request, "index.html", {'courses': courses})

def contact(request):
	return render(request, "contact.html")

def student_list(request):
    return render(request, "student_list.html")

def student_detail(request):
    return render(request, "student_detail.html")

class ContactView(TemplateView):
	template_name = "contact.html"

	def get_context_data(self, **kwargs):
		return {'page_title': 'Contact'}