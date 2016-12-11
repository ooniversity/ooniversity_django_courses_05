from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.core.mail import mail_admins, send_mail


class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('feedbacks:index')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(self.object.subject, self.object.message, self.object.from_email, settings.ADMINS)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return response