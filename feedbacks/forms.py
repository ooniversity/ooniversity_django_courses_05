from feedbacks.models import Feedback
from django import forms

class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['create_date']

