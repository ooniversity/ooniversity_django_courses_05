from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
def quadratic_results(request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    c=request.GET.get('c')
    d = b**2 - 4*a*c
    return d