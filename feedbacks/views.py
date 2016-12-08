from django.shortcuts import redirect
from django.urls import reverse
from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.core.mail import mail_admins


class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    form_class = FeedbackForm
    success_url = '/feedback/'

    def form_valid(self, form):
        response = super().form_valid(form)
        mail_admins(self.object.subject, self.object.message, fail_silently=False, connection=None, html_message=None)
        message = "Thank you for your feedback! We will keep in touch with you very soon!"
        messages.success(self.request, message)
        return response
