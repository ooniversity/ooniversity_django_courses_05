from django.contrib import admin
from students.models import Student
# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    search_fields = ["surname", "email"]
    list_display = ["full_name", "email", "skype"]
    list_filter = ["courses"]
    filter_horizontal = ['courses']
   # inlines = [LessonInline]

admin.site.register(Student, StudentsAdmin)
admin.site.site_header = "PyBursa Administration"


#class LessonInline(admin.StackedInline):
 #   model = Lesson
  #  list_fields = ["subject", "description", "order"]


