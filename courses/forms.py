from django import forms
from django.forms import ModelForm
from courses.models import Course, Lesson

class CourseModelForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'short_description', 'description', 'coach', 'assistant']

class LessonModelForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ['subject', 'description', 'course', 'order']