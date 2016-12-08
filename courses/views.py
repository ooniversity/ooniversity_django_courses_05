from django.shortcuts import render, redirect
from django.urls import reverse
from courses.forms import CourseModelForm, LessonModelForm
from courses.models import Course, Lesson
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_course = Course.objects.get(id=self.kwargs['pk'])
        lessons = Lesson.objects.filter(course=current_course).order_by('order')
        context['course'] = current_course
        context['lessons'] = lessons
        return context

class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = "courses/add.html"
    context_object_name = 'course'
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        form = super().form_valid(form)
        message = 'Course {} has been successfully added.' .format(self.object.name)
        messages.success(self.request, message)
        return form

class CourseUpdateView(UpdateView):
    model = Course
    template_name = "courses/edit.html"
    context_object_name = 'course'
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        message = 'The changes have been saved.'
        messages.success(self.request, message)
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('courses:edit', args = (self.object.pk,))

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = "courses/remove.html"
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Course deletion"
        courses = Course.objects.get(id=self.kwargs['pk'])
        context['name'] = courses
        return context

    def delete(self, request, *args, **kwargs):
        message = super().delete(request, *args, **kwargs)
        mess = 'Course {} has been deleted.' .format(self.object.name)
        messages.success(self.request, mess)
        return message

'''
def detail(request, course_id):
    current_course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=current_course).order_by('order')
    context = {'course': current_course, 'lessons': lessons}
    return render(request, 'courses/detail.html', context)

def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            result_string = "Course %(name)s has been successfully added." % {'name': instance.name}

            messages.success(request, result_string)
            return redirect('/')
    else:
        form = CourseModelForm()

    return render(request, 'courses/add.html', {'form': form})

def edit(request, course_id):

    course = Course.objects.get(id=course_id)

    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            instance = form.save()
            result_string = "The changes have been saved."
            messages.success(request, result_string)
            url_string = reverse('courses:edit', args=(course_id,))
            return redirect(url_string)

    form = CourseModelForm(instance=course)

    return render(request, 'courses/edit.html', {'form': form})

def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    name = course.name
    if request.method == "POST":
        course.delete()
        result_string = "Course %(name)s has been deleted." % {'name': name}

        messages.success(request, result_string)
        return redirect('/')

    delete_course = "Курс %(name)s будет удален" % {'name': name}

    return render(request, 'courses/remove.html', {'delete_course': delete_course})
'''

def add_lesson(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            mess = "Lesson %(subject)s has been successfully added." % {'subject': instance.subject}

            messages.success(request, mess)
            return redirect('/courses/{0}/'.format(course_id))
    else:
        form = LessonModelForm(initial={'course': course})

    return render(request, 'courses/add_lesson.html', {'form': form})

