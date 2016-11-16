from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def quadratic_results(request):

    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    x1 = 0
    x2 = 0
    descr = None

    if a != '0':
        if a.isdigit() and b.isdigit() and c.isdigit():
            if a != '' and b != '' and c != '':
                descr = int(b) ** 2 - 4 * int(a) * int(c)
                if descr > 0:
                    x1 = (-int(b) + descr ** (1/2)) / 2*int(a)
                    x2 = (-int(b) - descr ** (1/2)) / 2*int(a)
                elif descr == 0:
                    x1 = x2 = (-b) / (2*a)
    return render(request, 'quadratic/results.html', {'descr':descr, 'x1':x1, 'x2':x2, 'a':a, 'b':b, 'c':c})
