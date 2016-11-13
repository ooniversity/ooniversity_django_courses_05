import django.shortcuts
from django.http import HttpResponse
# Create your views here.
def quadratic_results(request, a, b, c):
	s = int(a) + int(b) + int(c)
	print('a=%s b=%s c=%s'%(a,b,c))
	return HttpResponse(s)
	#django.shortcuts.render(request, "results.html")