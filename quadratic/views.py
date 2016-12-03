from django.shortcuts import render
from .forms import QuadraticForm


def quadratic_results(request):
    if len(request.GET) > 0:
        form = QuadraticForm(request.GET)
        context = {'form': form, 'x1': '', 'x2': '', 'descr': ''}
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            if a != '0':
                context['descr'] = b ** 2 - 4 * a * c
                if context['descr'] > 0:
                    context['x1'] = (-b + context['descr'] ** (1/2)) / 2*a
                    context['x2'] = (-b - context['descr'] ** (1/2)) / 2*a
                elif context['descr'] == 0:
                    context['x1'] = context['x2'] = (-b) / (2*a)
    else:
        form = QuadraticForm()
        context = {"form": form}
    return render(request, 'quadratic/results.html', context)

    # try:
    #     int_a = int(a)
    #     int_b = int(b)
    #     int_c = int(c)
    # except ValueError:
    #     no_int = 'not empty'

    # if form.is_valid():
    #     if a != '0':
    #         if no_int == '':
    #             if a != '' and b != '' and c != '':
    #                 descr = int(b) ** 2 - 4 * int(a) * int(c)
    #                 if descr > 0:
    #                     x1 = (-int(b) + descr ** (1/2)) / 2*int(a)
    #                     x2 = (-int(b) - descr ** (1/2)) / 2*int(a)
    #                 elif descr == 0:
    #                     x1 = x2 = (-int(b)) / (2*int(a))

