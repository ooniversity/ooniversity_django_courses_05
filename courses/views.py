from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import UpdateView

from courses.forms import CourseModelForm, LessonModelForm
from .models import Course, Lesson


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['lessons'] = Lesson.objects.filter(course=pk)
        return context


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

    def form_valid(self, form):
        f = super().form_valid(form)
        messages.success(self.request, "Course {0} has been successfully added.".format(
            self.object.name))
        return f


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/edit.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        super().get_success_url()
        pk = self.kwargs['pk']
        return reverse('courses:edit', args=(pk,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def form_valid(self, form):
        f = super().form_valid(form)
        messages.success(self.request, "The changes have been saved.")
        return f


class CourseDeleteView(DeleteView):
    model = Course
    template_name = "courses/remove.html"
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        d = super().delete(request, *args, **kwargs)
        messages.success(request, "Course {0} has been deleted.".format(
            self.object.name))
        return d

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context


def add_lesson(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, "Lesson {0} has been successfully added.".format(
                lesson.subject))
            return redirect(reverse('courses:detail', args=(lesson.course.id,)))
    else:
        form = LessonModelForm(initial={"course": course.id})
    return render(request, 'courses/add_lesson.html', {'form': form})
