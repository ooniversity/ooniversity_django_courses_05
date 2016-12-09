from .models import Student
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentModelForm
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.urls import reverse_lazy


class StudenListView(ListView):
    model = Student

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            context = Student.objects.filter(courses=course_id)
        else:
            context = Student.objects.all()
        return context


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,
                         'Student {0} {1} has been successfully added'.format(
                                                            form.cleaned_data['name'],
                                                            form.cleaned_data['surname']))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Student registration'
        return context


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    template_name = 'students/edit.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Student info update'
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    template_name = 'students/remove.html'
    context_object_name = 'model'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        message = "Info on %(name)s %(surname)s has been successfully deleted." % {
            'name': self.object.name,
            'surname': self.object.surname
        }
        messages.success(self.request, message)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Student info suppression'

        return context

'''def create(request):
    if request.POST:
        model_form = StudentModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            messages.success(request,
                             'Student {0} {1} has been successfully added'.format(
                                                            model_form.cleaned_data['name'],
                                                            model_form.cleaned_data['surname']))
            return redirect('students:list_view')
    else:
        model_form = StudentModelForm()
    return render(request, "students/student_form.html", {"model": model_form})

def edit(request, student_id):
    student = Student.objects.get(id=int(student_id))
    if request.POST:
        model_form = StudentModelForm(request.POST, instance=student)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect('/students/edit/{0}/'.format(student_id))
    else:
        model_form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {"model": model_form})

def remove(request, student_id):
    student = Student.objects.get(id=int(student_id))
    if request.POST:
        student.delete()
        messages.success(request,
                         'Info on {0} {1} has been successfully deleted.'.format(student.name, student.surname))
        return redirect('students:list_view')
    else:
        return render(request, 'students/remove.html', {"model": student})'''