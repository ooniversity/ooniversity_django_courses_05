from django.contrib import admin
from .models import Student
from django.db import models
from django.forms import widgets

#class CourseInline(admin.StackedInline):
#    model = Course
#    fields = [('subject', 'description', 'order')]

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ['full_name' , 'email', 'skype']
    list_filter = ['courses']
    fieldsets = (
        ('Personal Info', {'fields': ('name', 'surname', 'date_of_birth')}),
        ('Contact Info', {'fields': ('email', 'phone', 'address', 'skype')}),
    )

admin.site.register(Student, StudentAdmin)

# Register your models here.
