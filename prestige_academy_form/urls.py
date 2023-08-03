from django.urls import path, include
from form_server import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.course_registration, name='course_registration'),
    path('success/', views.success, name='success'),  # Dodaj odnośnik do widoku 'success'
    
]
