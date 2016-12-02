from django.shortcuts import render
from quadratic.forms import QuadraticForm

def quadratic_results(request):
    if len(request.GET) > 0:
        form = QuadraticForm(request.GET)
        context =  {"discr": '',"x1": '', "x2": '', "form": form}
        if form.is_valid():
            print("isvalid")
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']	
            d=b**2 - 4*a*c
            if d >= 0:
                x1 = (-b+d**(1/2))/(2*a)
                x2 = (-b-d**(1/2))/(2*a)
                context['x1'] = x1
                context['x2'] = x2
            context['discr'] = d
            
    else:
        form = QuadraticForm()
        context =  {"form": form} 
        
    return render(request, "quadratic/results.html", context)





