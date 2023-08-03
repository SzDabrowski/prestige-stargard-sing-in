from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DanceCourseForm
from .models import DanceCourseType



def create_dance_course_types():
    # Ta funkcja tworzy początkową listę kursów tańca w bazie danych
    dance_course_types = [
        'Video klip dance kids 6-11 lat',
        'Video klip dance junior 12-16 lat',
        'Bachata Ladies',
        'Ladies styling',
        'Latino solo',
        'Kurs tańca towarzyskiego i użytkowego',
        'Bachata pary',
        'Taniec dla dzieci 4-5 lat small kids',
        'Taniec dla dzieci 6-7 lat Kids',
        'Taniec towarzyski sport 8-11 lat',
        'Taniec towarzyski sport 12-16 lat',
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
