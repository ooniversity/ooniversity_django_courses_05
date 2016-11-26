from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from courses.models import Course



class Detail(ListView):
    model = Course
    template_name = '../templates/courses/list.html'

    def get_queryset(self):
        return Course.objects.all()


class Course_descr_view(DetailView):
    model = Course
    template_name = '../templates/courses/detail.html'

