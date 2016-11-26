from django.contrib import admin
from .models import Course, Lesson

# Register your models here.

admin.site.register(Course)
admin.site.register(Lesson)

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    search_fields = ['name']
    inlines = [LessonInline]