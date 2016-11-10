from django.shortcuts import render

def result_quadratic(request, val = '111', a = '', b='', c=''):

    #if not isinstance(a, int):
    #    return render(request, 'quadratic/results.html' )
    print(val)
    print(a)
    print(b)
    print(c)
    return render(request, 'results.html')
