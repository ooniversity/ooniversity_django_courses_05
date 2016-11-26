from django.shortcuts import render
from .models import Course

def detail(request, pk):
    context = Course.objects.get(id=int(pk))
    return render(request, 'courses/detail.html', {'course': context})

