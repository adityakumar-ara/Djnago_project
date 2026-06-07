from django.shortcuts import render
from .models import student

def show_students(request):
    # Database se saare students nikal lo
    all_students = student.objects.all()
    
    # Unko ek dibbe (dictionary) me pack karo
    data = {
        'students': all_students
    }
    
    # Naye HTML page par bhej do
    return render(request, 'student_list.html', data)