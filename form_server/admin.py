from django.contrib import admin
from .models import Client, DanceCourseType

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_number', 'course_choice')
    list_filter = ('course_choice',)  # Dodaj pole filtrowania

class DanceCourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Client, ClientsAdmin)
admin.site.register(DanceCourseType, DanceCourseAdmin)