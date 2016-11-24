from django.contrib import admin
from .models import Course, Lesson
from django.db import models
from django.forms import widgets

class LessonInline(admin.StackedInline):
    model = Lesson
    fields = [('subject', 'description', 'order')]

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'short_description']
    fields = ['name', 'short_description', 'description']
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.site_header = 'PyBursa Administration'

# Register your models here.
