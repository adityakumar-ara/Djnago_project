from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def send_otp_email(email, otp):
    """Send an OTP email for email verification."""
    subject = 'Verify your email'
    message = f'Your OTP for email verification is {otp}. It will expire after one attempt.'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)


def register(request):
    if request.method == "POST":
        otp = request.POST.get('otp', '').strip()

        if otp:
            pending_registration = request.session.get('pending_registration')
            if not pending_registration:
                messages.error(request, 'OTP session expired. Please register again.')
                return redirect('register')

            if otp != pending_registration.get('otp'):
                messages.error(request, 'Invalid OTP. Please try again.')
                return render(request, 'register.html', {'otp_sent': True, 'email': pending_registration.get('email')})

            CustomeUser.objects.create_user(
                username=pending_registration['username'],
                email=pending_registration['email'],
                password=pending_registration['password'],
                full_name=pending_registration['full_name'],
            )
            request.session.pop('pending_registration', None)
            messages.success(request, 'Email verified successfully. Your account has been created.')
            return redirect('home')

        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')
        conform_password = request.POST.get('conform_password', '')
        form_data = {
            'full_name': full_name,
            'email': email,
        }
        if not full_name or not email or not password or not conform_password:
            messages.error(request, 'Fill all data')
            return render(request, 'register.html', form_data)
        if password != conform_password:
            messages.error(request, 'Your Password and Conform Password not Same, Password and Conform Password must be same')
            return render(request, 'register.html', form_data)
        if CustomeUser.objects.filter(email=email).exists():
            messages.error(request, 'This Email Already Exists')
            return render(request, 'register.html', form_data)

        username = email.split('@')[0]
        if CustomeUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'register.html', form_data)

        otp = str(random.randint(100000, 999999))
        request.session['pending_registration'] = {
            'full_name': full_name,
            'email': email,
            'password': password,
            'username': username,
            'otp': otp,
        }

        try:
            send_otp_email(email, otp)
        except Exception as exc:
            request.session.pop('pending_registration', None)
            messages.error(request, f'Unable to send OTP email: {exc}')
            return render(request, 'register.html', form_data)

        messages.success(request, 'OTP sent to your email. Please verify it to complete registration.')
        return render(request, 'register.html', {'otp_sent': True, 'email': email})

    return render(request, 'register.html')


def home(request):
    all_users = CustomeUser.objects.all()
    context = {
        'student': all_users,
    }
    return render(request, 'home.html', context)

def login(request):
    if request.method == "POST":
        email = request.POST.get('email','').strip().lower()
        password = request.POST.get('password','')
        if not email or not password:
           messages.error(request, "Plz Fill all first")
           return render(request, 'login.html')
        try:
           user_obj = CustomeUser.objects.get(email=email)
        except CustomeUser.DoesNotExist:
            user_obj = None 
        user = authenticate(
            request,
            username = user_obj.username if user_obj else email,
            password = password,
        )
        if user is None:
            messages.error(request,'Invalid email or password.')  
            return render(request, 'login.html')
        auth_login(request, user)
        messages.success(request, 'Login successful.')
        return redirect('/')
    return render(request, 'login.html')

def student_registration(request):
    if request.method == "POST":
        std_name = request.POST.get('std_name')
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        std_roll = request.POST.get('std_roll')
        std_no = request.POST.get('std_no')
        std_email = request.POST.get('std_email')
        std_address = request.POST.get('std_address')
        std_image = request.FILES.get('std_image')
        std_gender = request.POST.get('std_gender')
        student = Student.objects.create(
            std_name=std_name,
            course = course,
            branch = branch,
            semester = semester,
            std_roll =std_roll,
            std_no = std_no,
            std_email = std_email,
            std_address = std_address,
            std_image = std_image,
            std_gender = std_gender,
        )
        try:
            send_mail (
                subject="Student Registration Successful",
                 message=f"""
                 Hello {student.std_name},
                 Your registration has been completed successfully.
                 Student Details:
                 Name: {student.std_name}
                 Roll No: {student.std_roll}
                 Course: {student.course}
                 Branch: {student.branch}
                 Semester: {student.semester}

                 Thank you for registering.
                 Regards,
                 
                 Student Management System
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[student.std_email],
                fail_silently=False,
            )
            messages.success(
                request,
                "Student registered successfully. A confirmation email has been sent."
            )
        except Exception as e:
            print(e)
            messages.warning(
                request,
                "Student registered successfully, but the email could not be sent."
            )
        return redirect("student_registration")  
    return render(request, "student_registration.html")  