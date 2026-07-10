import random

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from .models import Branch, Course, CustomeUser, Student


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
    all_students = Student.objects.filter(is_deleted = False)
    context = {'students': all_students}
    return render(request, 'home.html', context)


def login(request):
    if request.method == "POST":
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')
        if not email or not password:
            messages.error(request, 'Plz Fill all first')
            return render(request, 'login.html')
        
        user = None
        try:
            # Find the user by email first
            user_obj = CustomeUser.objects.get(email=email)
            # Then, use the backend's authenticate method
            user = authenticate(request, username=user_obj.username, password=password)
        except CustomeUser.DoesNotExist:
            # User with this email doesn't exist, authentication will fail.
            pass
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('/')
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html')
    return render(request, 'login.html')


def student_registration(request):
    courses = Course.objects.all()
    branches = Branch.objects.all()

    if request.method == 'POST':
        std_name = request.POST.get('std_name', '').strip()
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester', '').strip()
        std_roll = request.POST.get('std_roll', '').strip()
        std_no = request.POST.get('std_no', '').strip()
        std_email = request.POST.get('std_email', '').strip().lower()
        std_address = request.POST.get('std_address', '').strip()
        std_dob = request.POST.get('std_dob', '').strip()
        gender = request.POST.get('gender', '').strip()
        std_image = request.FILES.get('std_image')
        
        student_info = {
            'std_name':std_name,
            'course':course,
            'branch':branch,
            'semester':semester,
            'std_roll':std_roll,
            'std_no':std_no,
            'std_email':std_email,
            'std_address':std_address,
            'std_dob':std_dob,
            'gender':gender,
        }
        if not all([std_name, course, branch, semester, std_roll, std_no, std_email, std_address, std_dob, gender]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'student_registration.html', {'courses': courses, 'branches': branches})
        if Student.objects.filter(std_email=std_email, is_deleted=False).exists():
            messages.error(request, 'This Email is already registered.')
            return render(request, 'student_registration.html', student_info)
        if Student.objects.filter(std_no=std_no, is_deleted=False).exists():
            messages.error(request, "This Phone Number is already registered.")
            return render(request, 'student_registration.html', student_info)
        if Student.objects.filter(std_roll=std_roll, is_deleted=False).exists():
            messages.error(request, "This Roll Number is already registered.")
            return render(request, 'student_registration.html', student_info)
        try:
            course_obj = Course.objects.get(id=course)
            branch_obj = Branch.objects.get(id=branch, course=course_obj)
        except (Course.DoesNotExist, Branch.DoesNotExist):
            messages.error(request, 'Please select a valid course and branch.')
            return render(request, 'student_registration.html', {'courses': courses, 'branches': branches})

        student = Student.objects.create(
            std_name=std_name,
            course=course_obj,
            branch=branch_obj,
            semester=int(semester),
            std_roll=std_roll,
            std_no=std_no,
            std_email=std_email,
            std_address=std_address,
            std_dob=std_dob,
            gender=gender,
            std_image=std_image,
            user=request.user if request.user.is_authenticated else None,
        )

        try:
            send_mail(
                subject='Student Registration Successful',
                message=f"""
                Hello {student.std_name},
                Your registration has been completed successfully.
                Student Details:
                Name: {student.std_name}
                Roll No: {student.std_roll}
                Course: {student.course.course_name}
                Branch: {student.branch.branch_name}
                Semester: {student.semester}

                Thank you for registering.
                Regards,
                Student Management System
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[student.std_email],
                fail_silently=False,
            )
            messages.success(request, 'Student registered successfully. A confirmation email has been sent.')
        except Exception as exc:
            print(exc)
            messages.warning(request, 'Student registered successfully, but the email could not be sent.')
        return redirect('student_registration')

    return render(request, 'student_registration.html', {'courses': courses, 'branches': branches})





def update_student_form(request,id):
    std = get_object_or_404(Student, id=id, user=request.user )
    if request.method == "POST":
        course = get_object_or_404(
            Course,
            id=request.POST.get("course")
        )

        branch = get_object_or_404(
            Branch,
            id=request.POST.get("branch")
        )
        std.std_name = request.POST.get('std_name')                
        std.course = course
        std.branch = branch
        std.semester = request.POST.get('semester')
        std.std_roll = request.POST.get('std_roll')
        std.std_no = request.POST.get('std_no')
        std.std_email = request.POST.get('std_email')
        std.std_address = request.POST.get('std_address')
        std.std_dob = request.POST.get('std_dob')
        std.gender = request.POST.get('gender')
        image = request.FILES.get('std_image')
        if image:
           std.std_image = image
        std.save()
        messages.success(request,'Student Update Successfully')
        return redirect('/')
    courses = Course.objects.all()
    branches = Branch.objects.all()
    return render(request, 'update_student.html', {'student': std, 'courses': courses, 'branches': branches})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id, user=request.user, is_deleted=False)

    student.is_deleted = True
    student.save()

    messages.success(request, "Student deleted successfully.")
    return redirect("home")