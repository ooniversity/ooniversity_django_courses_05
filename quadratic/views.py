from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.

def quadratic_results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']

    context = { 'var_a' : a, 'var_b' : b, 'var_c' : c }

    return render(request, 'results.html', context)