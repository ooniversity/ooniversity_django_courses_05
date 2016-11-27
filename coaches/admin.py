from django.contrib import admin
from .models import Coach

class CoachAdmin (admin.ModelAdmin):
    list_display = ('get_name', 'get_lastname', 'gender', 'skype', 'description')
    list_filter = ('user__is_staff',)

admin.site.register(Coach, CoachAdmin)
