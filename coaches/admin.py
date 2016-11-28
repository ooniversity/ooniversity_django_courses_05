from django.contrib import admin

# Register your models here.
from coaches.models import Coach

#class LessonInline(admin.StackedInline):
 #   model = Lesson
  #  list_fields = ["subject", "description", "order"]

class CoachAdmin(admin.ModelAdmin):
    list_display = ["user", "gender", "skype", "description"]
    #----------------------------------------------------------list_filter = ('is_staff',)---------------------------
  #  search_fields = ["name"]
 #   fields = ["name", "short_description"]
   # inlines = [LessonInline]

#class MyAdminSite(AdminSite):
 #   site_header = 'PyBursa Administration'

admin.site.register(Coach, CoachAdmin)
#admin.site.register(Lesson)