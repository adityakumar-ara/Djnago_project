from .models import Product_list, SignUp
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def product_list(request):
    products = Product_list.objects.all()
    
    return render(request,'product_list.html', {'products': products})

@login_required(login_url='login')
def add(request):
    if request.method =="POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        discription = request.POST.get('discription')
        quantity = request.POST.get('quantity')
        new_product = Product_list(
            name=name,
            price=price,
            image=image,
            description=discription,
            quantity=quantity
        )   
        new_product.save()
        return redirect('product_list')
    return render(request, 'add.html')


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            # 1. Default User save karein
            user = form.save()
            
            # 2. Aapka custom SignUp model data save karein
            SignUp.objects.create(
                user=user,
                phone=form.cleaned_data.get('phone'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name')
            )

            # 3. Email ki details taiyar karein
            user_email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            
            subject = 'Registration Successful - Aditya Store'
            message = f'Hi {username},\n\nThank you for joining us! Your account has been successfully created.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user_email]

            # 4. Email Bhejiye
            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                messages.success(request, "Account created and welcome email sent!")
            except Exception as e:
                # Agar email fail ho jaye toh error console mein dikhega par user redirect ho jayega
                print(f"Email Error: {e}")
                messages.warning(request, "Account created, but failed to send email.")

            return redirect('login')
        else:
            # Agar form invalid hai (e.g. Weak Password)
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})
    
@login_required(login_url='login')
def edit(request, id):
    updateproduct = get_object_or_404(Product_list, id=id)
    if request.method == "POST":
       updateproduct.name =request.POST.get('name')
       updateproduct.price =request.POST.get('price')
       if request.FILES.get('image'):
            updateproduct.image = request.FILES.get('image')
       updateproduct.description =request.POST.get('discription')
       updateproduct.quantity = request.POST.get('quantity')

       updateproduct.save()
       return redirect('product_list')
    context = {
        'product': updateproduct,
    }
    return render(request, 'edit.html', context)   

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request,f"welcome {username}!")
            return redirect('product_list')

        else:
            
            messages.error(request, "Invalid Name and Password")
            return redirect('login')
    return render(request, 'login.html')
     
@login_required(login_url='login')
def delete_product(request, id):
    product = get_object_or_404(Product_list, id=id)

    product.delete()
    
    messages.success(request, "Product deleted successfully!")
    return redirect('product_list')

from django.contrib.auth import logout # Ise top par import karein

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login') # Logout ke baad login page par bhej dein  



@login_required(login_url='login')
def profile_view(request):
    try:
        user_details = SignUp.objects.get(user=request.user)
    except SignUp.DoesNotExist:
        user_details = None
        
    return render(request, 'profile.html', {'user_details': user_details})       