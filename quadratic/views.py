from django.shortcuts import render
from django.http import HttpResponse

def quadratic_results(request):
    try:
        a = int(request.GET['a'])
        if a == 0: a = '0 коэффициент при первом слагаемом уравнения не может быть равень нулю'
    except:
        if request.GET['a'] == '': a = 'коэффициент не опеределен'
        else: a = 'коэффициент не целое число'
    try:
        b = int(request.GET['b'])
    except:
        if request.GET['b'] == '': b = 'коэффициент не опеределен'
        else: b = 'коэффициент не целое число'
    try:
        c = int(request.GET['c'])
    except:
        if request.GET['c'] == '': c = 'коэффициент не опеределен'
        else: c = 'коэффициент не целое число'
    if isinstance(a,int) and a != 0 and isinstance(b,int) and isinstance(c,int):
        d = b*b - 4*a*c
        if d > 0:
            x1 = (-b + d**(1/2))/ (2*a)
            x2 = (-b - d**(1/2)) / (2 * a)
            k = {'a': a, 'b': b, 'c': c, 'd': 'Дискриминант: '+str(d), 'x': 'Квадратное уравнение имеет два действительных корня: x1 = '+str(x1) +', x2 = '+str(x2) }
        if d == 0:
            x1 = (-b) / (2 * a)
            k = {'a': a, 'b': b, 'c': c, 'd': 'Дискриминант: ' + str(d),
                 'x': 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x1)}
        elif d < 0:
            k = {'a': a, 'b': b, 'c': c, 'd': 'Дискриминант: ' + str(d),
                 'x': 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных корней'}
    else:
        k = {'a': a, 'b': b, 'c': c}
    return render(request,'quadratic/results.html', k)