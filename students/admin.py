from django.contrib import admin
from students.models import Student
from django.forms import widgets

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ('full_name', 'email', 'skype')
    list_filter = ['courses']

    def full_name(self, obj):
        return ("%s %s" % (obj.name, obj.surname))


    #widgets.
    #full_name.short_description = 'Full name'

    fieldsets = (
        ('Personal info', {
            'fields': ('name', 'surname', 'date_of_birth')
        }),
        ('Contact info', {

            'fields': ('email', 'phone', 'address', 'skype', ),
        }),

        (None, {

            'fields': ('courses',),
        }),
    )

admin.site.register(Student, StudentAdmin)
