from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.

def quadratic_results(request):
    return render(request, 'results.html')