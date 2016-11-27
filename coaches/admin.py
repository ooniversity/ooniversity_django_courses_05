from django.contrib import admin
from .models import Coach
from django.contrib.auth.models import User


class CoachAdmin(admin.ModelAdmin):
    list_display = ['get_first_name', 'get_last_name', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff']

admin.site.register(Coach, CoachAdmin)


