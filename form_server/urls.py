from django.urls import path
from . import views

urlpatterns = [
    path('course_registration/', views.course_registration, name='course_registration'),
    path('success/', views.success, name='success'),
]
