from django.contrib import admin

# Register your models here.
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ["user", "gender", "skype", "description"]
    list_filter = ['user__is_staff',]

    def name(self, obj):
        return obj.user.first_name # не нужно и без него выводит

    def surname(self, obj):
        return obj.user.last_name


admin.site.register(Coach, CoachAdmin)
admin.site.site_header = "PyBursa Administration"
#admin.site.register(Lesson)