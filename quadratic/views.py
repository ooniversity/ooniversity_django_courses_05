from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from quadratic.forms import QuadraticForm


def valid(value):
     mes_value=''
     value_int=False
     if value:
        if ((value.isdigit() == True) or 
             ((len(value) > 1) and (value[0] == '-') and (value[1:].isdigit()) == True)):
            value_int = True

        if (value!='') and (value_int == False):
            mes_value='a'
     return [value_int, mes_value]


def quadratic_results(request):
    form = QuadraticForm()
    context =  {"form": form} 
    if len(request.GET) > 0:
        form = QuadraticForm(request.GET)
        (d, x1, x2) = (0, 0, 0)   
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']	
            ch = 0
            d=b**2 - 4*a*c
            if d>=0:
                x1=(-b+d**(1/2))/(2*a)
                x2=(-b-d**(1/2))/(2*a)
            context =  {"a": a, "b": b, "c": c, "discr": d,"x1": x1, "x2": x2, "form": form, "ch": ch}
    else:
        context =  {"form": form} 
    return render(request, "quadratic/results.html", context)





