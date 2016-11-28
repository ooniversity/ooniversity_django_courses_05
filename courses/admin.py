from django.contrib import admin
#from django.contrib.admin import AdminSite

# Register your models here.
from courses.models import Course, Lesson

class LessonInline(admin.TabularInline):
    model = Lesson
    list_fields = ["subject", "description", "order"]

#class CourseInline(admin.StackedInline):
    #model = Course
    #list_fields = ["coach", "assistant"]

class CourseAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    fields = ["name", "short_description", "coach", "assistant"]
    inlines = [LessonInline]

#class MyAdminSite(AdminSite):
 #   site_header = 'PyBursa Administration'

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.site_header = "PyBursa Administration"

