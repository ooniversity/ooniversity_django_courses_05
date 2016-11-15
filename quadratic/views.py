from django.shortcuts import render
def quadratic_results(request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    c=request.GET.get('c')
    d = b**2 - 4*a*c
    if d < 0:
            result_message = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
    elif d == 0:
        x = get_eq_root(a, b, d)
        result_message = "Дискриминант равен нулю, квадратное уравнение имеет один действительных корень: x1 = x2 = {}".format(x)
    else:
        x1 = get_eq_root(a, b, d)
        x2 = get_eq_root(a, b, d, order=2)
        result_message = "Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}".format(x1, x2)
    context.update({'d': d, 'result_message': result_message})
    return render(request, 'quadratic/results.html', context)