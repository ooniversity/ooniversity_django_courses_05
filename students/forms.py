from django import forms
from students.models import Student


class StudentModelForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        #widgets = {
        #            'date_of_birth': forms.DateInput(format='%d.%m.%Y'),
        #        }