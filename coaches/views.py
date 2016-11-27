from django.shortcuts import render
from .models import Coach

def detail(request, pk):
    context = Coach.objects.get(id=int(pk))
    print(context.user.first_name)
    return render(request, 'coaches/detail.html', {'coach': context})
