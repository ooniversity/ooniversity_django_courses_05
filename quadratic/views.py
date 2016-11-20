from django.shortcuts import render
from django.http import HttpResponse

def quadratic_results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    answer = int(a)  + int(b) + int(c)
    return render(request, "results.html", {"answer": answer})


