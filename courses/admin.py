from django.contrib import admin
from .models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    search_fields = ['name']
    inlines = [LessonInline]


admin.site.register(Course, CoursesAdmin)
admin.site.register(Lesson)
