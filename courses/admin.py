from django.contrib import admin
from .models import Lesson, Course
class LessonAdmin(admin.ModelAdmin):
	list_display = ["subject", "course"]

# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
