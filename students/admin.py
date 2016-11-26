from django.contrib import admin
from students.models import Student
# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    search_fields = ["surname", "email"]
    list_display = ["full_name", "email", "skype"]
    list_filter = ["courses"]
   # inlines = [LessonInline]

admin.site.register(Student, StudentsAdmin)


#class LessonInline(admin.StackedInline):
 #   model = Lesson
  #  list_fields = ["subject", "description", "order"]


