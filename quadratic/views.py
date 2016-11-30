from django.shortcuts import render, redirect
from .forms import QuadraticForm

def quadratic_results(request):
    if request.GET:
        form = QuadraticForm(request.GET)
        context = {
            "diskr": "",
            "Form": form
        }
        if form.is_valid():
            a = int(form.cleaned_data['a'])
            b = int(form.cleaned_data['b'])
            c = int(form.cleaned_data['c'])
            diskr = b * b - 4 * a * c
            context['diskr'] = "Дискриминант: {0}".format(diskr)
            if diskr < 0:
                context["info_text"] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif diskr == 0:
                x1 = -b / 2 * a
                context[
                    "info_text"] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0}".format(
                    x1)
            else:
                x1 = (-b + diskr ** (1 / 2)) / 2 * a
                x2 = (-b - diskr ** (1 / 2)) / 2 * a
                context["info_text"] = "Квадратное уравнение имеет два действительных корня: x1 = {0}, x2 = {1}".format(
                    x1, x2)
    else:
        form = QuadraticForm()
        context = {'Form': form}
    return render(request, 'quadratic/results.html', context)
