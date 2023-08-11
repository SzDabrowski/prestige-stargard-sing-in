from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DanceCourseForm
from .models import DanceCourseType



def create_dance_course_types():
    # Ta funkcja tworzy początkową listę kursów tańca w bazie danych
    dance_course_types = [
        'Video klip Dance Kids 6-11 lat',
        'Bachata w parach',
        'Taniec Towarzyski Sport 8-11 lat',
        'Taniec Towarzyski Sport 12-16 lat',
        'Taniec dla dzieci Prestige  Kids 4-5 lat',
        'Taniec dla dzieci Prestige Junior 6-7 lat',
        'Latino Solo',
        'Ladies Styling',
        'Latino Sport'
    ]

    for course_type in dance_course_types:
        DanceCourseType.objects.get_or_create(name=course_type)

def course_registration(request):
    create_dance_course_types() 
    if request.method == 'POST':
        form = DanceCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Przekierowanie po pomyślnym zapisie
    else:
        form = DanceCourseForm()

    available_courses = DanceCourseType.objects.all()

    return render(request, 'course_registration.html', {'form': form, 'available_courses': available_courses})

def success(request):
    return render(request, 'success.html')
