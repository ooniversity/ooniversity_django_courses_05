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
    if not error_a and int(a) == 0:
        error_a = error_if_zero

    b = request.GET['b']
    error_b = check_input_data(b)
    c = request.GET['c']
    error_c = check_input_data(c)

    if not error_a and not error_b and not error_c:
        a = int(a)
        b = int(b)
        c = int(c)
        d = b * b - 4 * a * c

    if d:
        d_text = "Дискриминант: {0}".format(d)
    else:
        d_text = ""
        

    

    context = { 'var_a' : a, 'var_b' : b, 'var_c' : c, 'error_c' : error_c, 'error_b' : error_b, 'error_a' : error_a, 'd' : d_text }

    return render(request, 'results.html', context)