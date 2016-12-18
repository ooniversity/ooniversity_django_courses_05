from django.contrib import admin
from feedbacks.models import Feedback

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    fields = ["name", "subject", "message", "from_email"]
    list_display = ["from_email", "create_date"]


admin.site.register(Feedback, FeedbackAdmin)