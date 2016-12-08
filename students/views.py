from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class StudentListView(ListView):
    model = Student
    context_object_name = "students"

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        if self.request.method == 'POST':
            application = form.save()
            message = u'Student {} {} has been successfully added.' .format(application.name, application.surname)
            messages.success(self.request, message)
        return super().form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        if self.request.method == 'POST':
            application = form.save()
            message = 'Info on the student has been sucessfully changed.'
            messages.success(self.request, message)
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('students:edit', args = (self.object.pk,))

class StudentDeleteView(DeleteView):
    model = Student
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        application = Student.objects.get(id=self.kwargs['pk'])
        context['delete_student'] = "Студент %(name)s %(surname)s будет удален" % {'name': application.name, 'surname': application.surname}
        return context

    def get_success_url(self, **kwargs):
        application = Student.objects.get(id=self.kwargs['pk'])
        if self.request.method == 'POST':
            application.delete()
            message = 'Info on {} {} has been sucessfully deleted.' .format(application.name, application.surname)
            messages.success(self.request, message)
            return reverse_lazy('students:list_view')
        return reverse_lazy('students:remove')

'''
def list_view(request):

    if len(request.GET) == 0:
        student_list = Student.objects.all()
    else:
        course_id = request.GET['course_id']
        student_list = Student.objects.filter(courses__id=course_id)

    context = {'students': student_list}
    return render(request, 'students/list.html', context)


def detail(request, student_id):
    current_student = Student.objects.get(id=student_id)
    context = {'student': current_student}
    return render(request, 'students/detail.html', context)

def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            result_string = "Student %(name)s %(surname)s has been successfully added." % {'name': instance.name,
                                                                                           'surname': instance.surname}

            messages.success(request, result_string)
            return redirect('/students/')
    else:
        form = StudentModelForm()

    return render(request, 'students/add.html', {'form': form})

def edit(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            instance = form.save()
            result_string = "Info on the student has been successfully changed."
            messages.success(request, result_string)
            url_string = reverse('students:edit', args=(student_id,))
            return redirect(url_string)

    form = StudentModelForm(instance=student)

    return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    name = student.name
    surname = student.surname
    if request.method == "POST":
        student.delete()
        result_string = "Info on %(name)s %(surname)s has been successfully deleted." % {'name': name,
                                                                                         'surname': surname}
        messages.success(request, result_string)
        return redirect('/students/')

    delete_student = "Студент %(name)s %(surname)s будет удален" % {'name': name,
                                                                    'surname': surname}

    return render(request, 'students/remove.html', {'delete_student': delete_student})
'''

