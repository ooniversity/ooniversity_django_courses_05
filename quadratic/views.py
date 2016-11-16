from django.shortcuts import render
from django.http import HttpResponse

def proverka(x):
    if x:
        try:
            y = int(x)
        except ValueError:
            y = x + '\r\n коэффициент не целое число'
    else:
        y = ' коэффициент не определен'
    return y

def quadratic_results(request):
    numbers = {}

    a = proverka(request.GET['a'])
    b = proverka(request.GET['b'])
    c = proverka(request.GET['c'])
   
    if isinstance(a,int) and isinstance(b,int) and isinstance(c,int):
        if a == 0:
            a_rez = '0 коэффициент при первом слагаемом уравнения не может быть равным нулю'
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

    numbers.update({ 'a' : a, 'b' : b, 'c' : c })
    return render(request, 'results.html', numbers)
