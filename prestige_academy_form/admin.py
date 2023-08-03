from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from ..form_server.models import Client, DanceCourseType

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_number', 'course_choice', 'get_edit_link')
    list_filter = ('course_choice',)  # Dodaj pole filtrowania

    def get_edit_link(self, obj):
        return format_html('<a href="{}">Edytuj</a>', reverse('admin:%s_%s_change' % (obj._meta.app_label,  obj._meta.model_name),  args=[obj.pk]))

    get_edit_link.short_description = 'Edycja'

class DanceCourseAdmin(admin.ModelAdmin):
    list_display = ('name')

    def get_edit_link(self, obj):
        return format_html('<a href="{}">Edytuj</a>', reverse('admin:%s_%s_change' % (obj._meta.app_label,  obj._meta.model_name),  args=[obj.pk]))

    get_edit_link.short_description = 'Edycja'

admin.site.register(Client, ClientsAdmin)
admin.site.register(DanceCourseType, DanceCourseAdmin)
