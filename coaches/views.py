from django.shortcuts import render
from .models import Coach

def detail(request, pk):
    context = Coach.objects.get(id=int(pk))
    return render(request, 'coaches/detail.html', {'coach': context})
