from django import forms
from django.forms import ModelForm
from students.models import Student

class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'address', 'skype', 'courses']
