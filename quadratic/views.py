#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render

def quadratic_results(request, a, b, c):

    try:
        int_a = int(a)
    except ValueError:
        message_int_a = 'коэффициент не целое число'
        message_int = 'коэффициент не целое число'

    try:
        int_b = int(b)
    except ValueError:
        message_int_b = 'коэффициент не целое число'
        message_int = 'коэффициент не целое число'

    try:
        int_c = int(c)
    except ValueError:
        message_int_c = 'коэффициент не целое число'
        message_int = 'коэффициент не целое число'

    if a == '' or b == '' or c == '':
        message_not_arg = 'коэффициент не определен'

    if a == '0':
        message_null = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

    if message_int == '' and message_not_arg == '' and message_null == '':
        descr = int_b ** 2 - 4 * int_a * int_c
        if descr > 0:
            x1 = (-int_b + descr ** (1/2)) / 2*int_a
            x2 = (-int_b - descr ** (1/2)) / 2*int_a
            descr_message = 'Квадратное уравнение имеет два действительных корня:'
        elif descr == 0:
            x1 = x2 = (-b) / (2*a)
            descr_message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень:'
        else:
            descr_message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    return (request, 'results.html', message_int_a, message_int_b, message_int_c, descr, x1, x2)
