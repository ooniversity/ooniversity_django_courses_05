import django.shortcuts, math
from django.http import HttpResponse
from django.shortcuts import render
# -*- coding: utf-8 -*-

from django import forms

class QuadraticForm(forms.Form):
  a = forms.CharField(max_length=10)
  b = forms.CharField(max_length=10)
  c = forms.CharField(max_length=10)


# Create your views here.
def quadratic_results(request):
    form = QuadraticForm()
    a=request.GET.get('a')
    b=request.GET.get('b')
    c=request.GET.get('c')
    context = {'error': False}
    context['form'] = form
    d=request.GET
    for key, value in d.items():
        try:
            if value == "":
                print("%s \n коэффициент не определен" %value)
            elif int(value):
                value=int(value)
                print("%s=%s" %(key,value))
            else:
                print("%s= \n коэффициент не целое число" %key)
        except ValueError:
            print("GOOD!")
            Exit(1)
    a = int(a)
    b = int(b)
    c = int(c)
    x1=0
    x2=0
    if a == 0:
        print("a=0 \n коэффициент при первом слагаемом уравнения не может быть равным нулю")
        try:
            a = 0
        except ZeroDivisionError:
            print("a=0 \n коэффициент при первом слагаемом уравнения не может быть равным нулю")
            Exit(1)
    else:
        discrimin = b ** 2 - 4 * a * c
        print("Дискриминант: %d" % discrimin)
        if discrimin > 0:
            x1 = (-b + math.sqrt(discrimin)) / (2 * a)
            x2 = (-b - math.sqrt(discrimin)) / (2 * a)
            print("Квадратное уравнение имеет два действительных корня: x1 = %.2f, x2 = %.2f" % (x1, x2))
        elif discrimin == 0:
            x = -b / (2 * a)
            print("Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.2f" % x)
        else:
            print("Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.")
    return render(request, 'quadratic/results.html', {"discr": discrimin, "x1": x1, "x2":x2, "a":a, "b":b, "c":c})