from django.contrib import admin
from students.models import Student



class StudentAdmin (admin.ModelAdmin):
    list_display = ('full_name', 'email', 'skype')
    search_fields = ('surname', 'email',)
    list_filter = ('courses',)
    filter_horizontal = ('courses',)
    #inlines = (LessonInline,)
    fieldsets = (
        ('Personal info', {
            'fields': ('name', 'surname', 'date_of_birth')
        }),
        ('Contact info', {
            'fields': ('email', 'phone', 'address', 'skype')
        }),
        (None, {
            'fields': ('courses',)
        })
    )

admin.site.register(Student, StudentAdmin)
