from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .forms import StudentRegistration,BasicSignupForm
from django.contrib import messages
from django.db.models import Q # <--- Ye zaroori hai
from .models import *
# Create your views here.
def create_student(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentRegistration()  
    return render(request, 'add_student.html',{'form':form})      

def show_student(request):
    students = Student.objects.all()   
    return render (request, 'show.html', {'students':students})   



from django.contrib import messages
from .forms import BasicSignupForm # Apna naya simple form import karein

def student_signup(request):
    if request.method == 'POST':
        form = BasicSignupForm(request.POST) 
        
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('/') 
    else:
        form = BasicSignupForm()
        
    return render(request, 'student_signup.html', {'form': form})


from django.core.paginator import Paginator
from django.db.models import Q

def show_student(request):
    query = request.GET.get('search_query', '').strip()
    
    # 1. QuerySet filter aur order karein (Quotes zaroori hain)
    if query:
        student_list = Student.objects.filter(
            Q(std_name__icontains=query) | 
            Q(std_roll__icontains=query) | 
            Q(std_village__icontains=query) |
            Q(department__name__icontains=query) |
            Q(course__name__icontains=query)
        ).distinct().order_by('id') # <--- Yahan 'id' quotes mein hai
    else:
        student_list = Student.objects.all().order_by('id') # <--- Yahan bhi

    # 2. Paginator ko QuerySet pass karein
    paginator = Paginator(student_list, 10) 
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    return render(request, 'show.html', {
        'students': students, 
        'query': query
    })


from django.core.mail import send_mail
from django.http import HttpResponse

def send_user_email(request):
    send_mail(
        'Subject: Welcome to Our Company',
        'Hello User, ye aapka message hai.',
        'adityaara7667@gmail.com',
        ['funnwithaditya@gemail.com'],
        fail_silently=False,
    )