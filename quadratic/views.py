from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.
def check_input_data(value):
    error = ""
    error_if_not_int = "коэффициент не целое число"
    error_if_empty = "коэффициент не определен"


    if len(value) == 0:
        error = error_if_empty
    else:
        try:
        	a = int(value)
        except:
        	error = error_if_not_int
    return(error)


def quadratic_results(request):

    error_if_zero = "коэффициент при первом слагаемом уравнения не может быть равным нулю"

    a = request.GET['a']
    error_a = check_input_data(a)
    if int(a) == 0:
        error_a = error_if_zero

    b = request.GET['b']
    error_b = check_input_data(b)
    c = request.GET['c']
    error_c = check_input_data(c)




    

    context = { 'var_a' : a, 'var_b' : b, 'var_c' : c, 'error_c' : error_c, 'error_b' : error_b, 'error_a' : error_a }

    return render(request, 'results.html', context)