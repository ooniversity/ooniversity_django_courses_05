from django.shortcuts import render
from django.http import HttpResponse

def proverka(x):
    mess = ''
    zn = ''
    if x:
        try:
            zn = int(x)
        except ValueError:
            zn = x
            mess = 'коэффициент не целое число'
    else:
        mess = 'коэффициент не определен'
    return {'zn':zn, 'mess':mess}

def quadratic_results(request):
    numbers = {}

    dicta = proverka(request.GET['a'])
    a = dicta['zn']
    dictb = proverka(request.GET['b'])
    b = dictb['zn']
    dictc = proverka(request.GET['c'])
    c = dictc['zn']   
    if isinstance(a,int) and isinstance(b,int) and isinstance(c,int):
        if a == 0:
            dicta['mess'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        else:
            d = b ** 2 - 4 * a * c
            if d < 0:
                result = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif d == 0:
                result = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %0.1f" % (-b / 2 * a)
            else:
                x1 = (-b + d ** (1/2.0)) / (2 * a)
                x2 = (-b - d ** (1/2.0)) / (2 * a)
                result = "Квадратное уравнение имеет два действительных корня: x1 = %0.1f, x2 = %0.1f" % (x1, x2)
            numbers.update({ 'd' : d, 'result' : result })

    numbers.update({ 'a' : dicta, 'b' : dictb, 'c' : dictc })
    return render(request, 'results.html', numbers)
