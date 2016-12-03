from django.shortcuts import render
from .form import QuadraticForm
from .quadratic import discriminant

def quadratic_results(request):
    form = QuadraticForm()

    context = {}
    if len(request.GET) > 0:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            dict_discriminant = discriminant(form.cleaned_data)
            context.update(dict_discriminant)

    context['form'] = form

    return render(request, 'quadratic/results.html', context)

#"This equation has one solutions: "
#"This equation has two solutions: ", x1, " or", x2
#"This equation has no real solution"
