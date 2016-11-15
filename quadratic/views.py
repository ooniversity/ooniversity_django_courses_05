from django.shortcuts import render
from django.http import HttpResponse

def quadratic_results(request):
    try:
        a = int(request.GET['a'])
        if a == 0: a = '0<br/>коэффициент при первом слагаемом уравнения не может быть равным нулю'

    except:
        if request.GET['a'] == '': a = '<br/>коэффициент не определен'
        else: a = request.GET['a'] + '<br/>коэффициент не целое число'
    try:
        b = int(request.GET['b'])
    except:
        if request.GET['b'] == '': b = '<br/>коэффициент не определен'
        else: b = request.GET['b'] + '<br/>коэффициент не целое число'
    try:
        c = int(request.GET['c'])
    except:
        if request.GET['c'] == '': c = '<br/>коэффициент не определен'
        else: c = request.GET['c'] + '<br/>коэффициент не целое число'
    if isinstance(a,int) and a != 0 and isinstance(b,int) and isinstance(c,int):
        d = b*b - 4*a*c
        if d > 0:
            x1 = round((-b + d**(1/2))/ (2*a),1)
            x2 = round((-b - d**(1/2)) / (2 * a),1)
            k = {'a': a, 'b': b, 'c': c, 'd': 'Дискриминант: '+str(d), 'x': 'Квадратное уравнение имеет два действительных корня: x1 = '+str(x1) +', x2 = '+str(x2) }
        if d == 0:
            x1 = (-b) / (2 * a)
            k = {'a': a, 'b': b, 'c': c, 'd': 'Дискриминант: ' + str(d),
                 'x': 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x1)}
        elif d < 0:
            k = {'a': a, 'b': b, 'c': c, 'd': 'Дискриминант: ' + str(d),
                 'x': 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'}
    else:
        k = {'a': a, 'b': b, 'c': c}
    return render(request, 'results.html', k)