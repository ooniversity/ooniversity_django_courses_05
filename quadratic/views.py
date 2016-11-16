from django.shortcuts import render


class Koeff(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.value_int = None
        self.error_message = None

    def is_valid(self):
        if not self.value:
            self.error_message = "коэффициент не определен"
            return False

        try:
            self.value_int = int(self.value)
        except ValueError:
            self.error_message = "коэффициент не целое число"
            return False

        if self.name == 'a' and self.value_int == 0:
            self.error_message = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
            return False
        return True


def get_d(a, b, c):
    d = b**2 - 4*a*c
    return d


def get_eq_root(a, b, d, order=1):
    if order == 1:
        x = (-b + d**(1/2.0)) / 2*a
    else:
        x = (-b - d**(1/2.0)) / 2*a
    return x


def quadratic_results(request):
    diskr = {'error': False}
    for name_value in ['a', 'b', 'c']:
        koeff = koeff(name_value, request.GET.get(name_value, ''))
        if koeff.is_valid():
            diskr[name_value] = koeff.value_int
        else:
            diskr['error'] = True
            diskr[name_value + '_error'] = koeff.error_message
            diskr[name_value] = koeff.value
    if not diskr['error']:
        a = diskr['a']
        b = diskr['b']
        c = diskr['c']
        d = get_d(a, b, c)
        if d < 0:
            answer = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif d == 0:
            x = get_eq_root(a, b, d)
            answer = "Дискриминант равен нулю, квадратное уравнение имеет один действительных корень: x1 = x2 = {}".format(x)
        else:
            x1 = get_eq_root(a, b, d)
            x2 = get_eq_root(a, b, d, order=2)
            answer = "Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}".format(x1, x2)

        diskr.update({'d': d, 'answer': answer})
    return render(request, 'quadratic/results.html', diskr)