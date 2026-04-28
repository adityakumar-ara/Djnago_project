# Create your views here.

from django.shortcuts import render, redirect
from .models import Student

# READ (Show all students)
def home(request):
    students = Student.objects.all()
    return render(request,'home.html', {'students': students})


# CREATE (Add student)
def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        image = request.FILES.get('image')
        email = request.POST.get('email')
        city = request.POST.get('city')

        Student.objects.create(
            std_name=name,
            std_roll=roll,
            std_image=image,
            std_email=email,
            std_city=city
        )
        return redirect('home')

    return render(request,'add_student.html')


# UPDATE
def update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.std_name = request.POST.get('name')
        student.std_roll = request.POST.get('roll')
        if request.FILES.get('image'):
            student.std_image = request.FILES.get('image')
            student.std_email = request.POST.get('email')
            student.std_city = request.POST.get('city')
        student.save()

        return redirect('home')

    return render(request,'update_student.html', {'student': student})


# DELETE
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')
