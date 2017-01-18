from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.conf import settings

from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback


class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')
    form_class = FeedbackForm

    def form_valid(self, form):
        s = super().form_valid(form)
        messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        send_mail(self.object.subject, self.object.message, self.object.from_email, settings.ADMINS)
        return s

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create feedback'
        context['button'] = 'Отправить'
        return context
