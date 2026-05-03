from django.shortcuts import render,redirect
from .forms import StudentRegistration,  student_signup
from django.contrib import messages
from .models import*
# Create your views here.
def create_student(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentRegistration()  
    return render(request, 'add_student.html',{'form':form,})      

def show_student(request):
    students = Student.objects.all()   
    return render (request, 'show.html', {'students':students})   

def student_signup(request):
    if request.method == 'POST':
        form = Student_signup(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successfull")
            return redirect('/')
    else:
        form = Student_signup()
    return render(request, 'student_signup.html',{'form':form})