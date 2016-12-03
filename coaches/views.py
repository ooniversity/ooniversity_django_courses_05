from django.shortcuts import render, render_to_response
from coaches.models import Coach
from courses.models import Course

# Create your views here.

def detail(request, coach_id):
    coach_name = Coach.objects.get(id = coach_id)
    coach = Course.objects.filter(coach = coach_name.id)
    assistant = Course.objects.filter(assistant = coach_name.id)
    return render(request, 'coaches/templates/coaches/detail.html', {'coach_name': coach_name,
                                                                     'coach': coach,
                                                                     'assistant': assistant})
