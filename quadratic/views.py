from django.shortcuts import render

def check(num):
    try:
        if not num:
            return "", "коэффициент не определен"
        elif int(num) == 0:
            return 0, ""
        elif int(num):
            return int(num), ""
    except :
        return num, "коэффициент не целое число"

from django import forms

class QuadraticForm(forms.Form):
    a = forms.CharField(max_length=10)
    b = forms.CharField(max_length=10)
    c = forms.CharField(max_length=10)
        

def quadratic_results(request):
    a, prefix_a = check(request.GET.get('a'))
    b, prefix_b = check(request.GET.get('b'))
    c, prefix_c = check(request.GET.get('c'))
    dict_html = {
        "a": a, "prefix_a": prefix_a or "",
        "b": b, "prefix_b": prefix_b or "",
        "c": c, "prefix_c": prefix_c or "",
        "diskr": "",
        "info_text": ""
    }
    form = QuadraticForm()
    dict_html['form'] = form
    if isinstance(a, int) and a != 0 and (b or b == 0) and (c or c == 0):
        diskr = b * b - 4 * a * c
        dict_html['diskr'] = "Дискриминант: {0}".format(diskr)
        if diskr < 0:
                dict_html["info_text"] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif diskr == 0:
            x1 = -b / 2 * a
            dict_html["info_text"]= "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0}".format(x1)
        else:
            x1 = (-b + diskr ** (1 / 2)) / 2 * a
            x2 = (-b - diskr ** (1 / 2)) / 2 * a
            dict_html["info_text"] = "Квадратное уравнение имеет два действительных корня: х1 = {0}, х2 = {1}".format(x1, x2)
    elif a == 0:
        dict_html["prefix_a"] = "Коэффициент при первом слагаемом уравнения не может быть равным нулю"
        dict_html["diskr"] = ""
    return render(request, 'quadratic/results.html', dict_html)
    return render(request, 'quadratic/results.html')
# Create your views here.
