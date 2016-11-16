from django.shortcuts import render


def quadratic_results(request):

    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    x1 = 0
    x2 = 0
    descr = None
    no_int = ''

    try:
        int_a = int(a)
        int_b = int(b)
        int_c = int(c)
    except ValueError:
        no_int = 'not empty'

    if a != '0':
        if no_int == '':
            if a != '' and b != '' and c != '':
                descr = int(b) ** 2 - 4 * int(a) * int(c)
                if descr > 0:
                    x1 = (-int(b) + descr ** (1/2)) / 2*int(a)
                    x2 = (-int(b) - descr ** (1/2)) / 2*int(a)
                elif descr == 0:
                    x1 = x2 = (-int(b)) / (2*int(a))
    return render(request, 'quadratic/results.html', {'descr':descr, 'x1':x1, 'x2':x2, 'a':a, 'b':b, 'c':c})
