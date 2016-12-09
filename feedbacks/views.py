from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.conf import settings

from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback


class Feedback(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')
    form_class = FeedbackForm

    def form_valid(self, form):
        s = super().form_valid(form)
        send_mail(form.cleaned_data['subject'],form.cleaned_data['message'],
                   form.cleaned_data['from_email'], recipient_list=settings.ADMINS,)
        messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        return s

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create feedback'
        context['button'] = 'Отправить'
        return context
