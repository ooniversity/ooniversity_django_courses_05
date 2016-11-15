import django.shortcuts, math
from django.http import HttpResponse
# -*- coding: utf-8 -*-

# Create your views here.
def quadratic_results(request):
	a=request.GET.get('a')
	b=request.GET.get('b')
	c=request.GET.get('c')
	d=request.GET
	if (a not int) or (b not int) or (c not int):
		try:
			a = int(a)
			b = int(b)
			c = int(c)
		except ValueError:
			print("коэффициент не целое число")
		finally:
			print("коэффициент не целое число")
			Exit(1)

	a = int(a)
	b = int(b)
	c = int(c)
	# if a =='':
	print(type(a))
	if a == 0:
		print("a=0 \n коэффициент при первом слагаемом уравнения не может быть равным нулю")
		try:
			a = 0
		except ZeroDivisionError:
			print("a=0 \n коэффициент при первом слагаемом уравнения не может быть равным нулю")
			Exit(1)
	else:
		discrimin = b ** 2 - 4 * a * c
		print("Дискриминант: %d" % discrimin)
		if discrimin > 0:
			x1 = (-b + math.sqrt(discrimin)) / (2 * a)
			x2 = (-b - math.sqrt(discrimin)) / (2 * a)
			print("Квадратное уравнение имеет два действительных корня: x1 = %.2f, x2 = %.2f" % (x1, x2))
		elif discrimin == 0:
			x = -b / (2 * a)
			print("Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.2f" % x)
		else:
			print("Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.")
	return HttpResponse('Квадратное уравнение а*х*х + b*x + c = 0 ')

	#django.shortcuts.render(request, "results.html")