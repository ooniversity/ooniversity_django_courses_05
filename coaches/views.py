from django.shortcuts import get_object_or_404, render
from .models import Coach


def detail(request, pk):
    coach = get_object_or_404(Coach, pk=pk)
    return render(request, 'coaches/detail.html', {'coach': coach})

