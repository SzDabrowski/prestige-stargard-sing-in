from django import forms
from .models import Client

class DanceCourseForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'contact_number', 'course_choice']
