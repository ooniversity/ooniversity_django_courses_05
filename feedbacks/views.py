from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from feedbacks.models import Feedback
from django.core.mail import mail_admins

class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedbacks/feedback.html'
    context_object_name = 'feedback'
    success_url = reverse_lazy('feedback')
    fields = "__all__"

    def form_valid(self, form):
        message = super().form_valid(form)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        mail_admins(self.object.subject, self.object.message)
        return message
