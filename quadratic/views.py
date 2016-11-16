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
    d_text = ""
    d_error = ""
    d_lover_zero = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."

    info = ""
    info_if_one = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: "
    info_if_two = "Квадратное уравнение имеет два действительных корня: "

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

        
        d_text = "Дискриминант: {0}".format(d)
        if d < 0:
            d_error = d_lover_zero
        elif d == 0:
            x1 = -b / 2 * a
            info = info_if_one + "x1 = x2 = {0}".format(x1)
        else:
            x1 = (-1*b + d ** (1 / 2)) / 2 * a
            x2 = (-1*b - d ** (1 / 2)) / 2 * a
            info = info_if_two + "х1 = {0}, х2 = {1}".format(x1, x2)

    context = { 'var_a' : a, 'var_b' : b, 'var_c' : c, 'error_c' : error_c, 'error_b' : error_b, 'error_a' : error_a, 'd' : d_text, 'd_error' : d_error, 'info' : info }

    return render(request, 'results.html', context)