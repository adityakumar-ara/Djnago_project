from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post

def signup_view(request):
    if request.method == "POST":
       username = request.POST.get('username')
       password = request.POST.get('password')
       password_confirmation = request.POST.get('password_confirmation')

    #    check Password must be same?
       if password != password_confirmation:
           messages.error(request, "Your Password not match!")
           return redirect('signup_view')
       
    #    check username alredy exists 

       if User.objects.filter(username=username).exists():
           messages.error(request, "Username alredy exists")
           return redirect ('signup_view')

       user = User.objects.create_user(username=username, password=password)  
       user.save()

       messages.success(request, "SignUp Successful")
       return redirect('login_view')
    return render(request, 'signup.html')    

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {username}!")
            return redirect('post_list')
        else:
            
            messages.error(request, "Invalid Username and Password")
            return redirect('login_view')
    return render(request, 'login.html')    
 
@login_required
def post_list(request):
    all_posts = Post.objects.all().order_by('-created_at') 
    return render(request, 'feed.html', {'posts': all_posts})


@login_required
def create_post(request):
    if request.method == "POST":
        text_content = request.POST.get('text')
        # Check karo ki kahin user ne khali button toh nahi daba diya
        if text_content :
            Post.objects.create(user = request.user, text= text_content)
            messages.success(request, "Your Bubble was Posted Successfully")
        return redirect('post_list')    
    return render(request, 'create_post.html')

@login_required(login_url='login_view')
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user != request.user:
        return redirect('post_list')
    if request.method == "POST":
        updated_text = request.POST.get('text')
        post.text = updated_text
        post.save() 
        return redirect('post_list')

    return render(request, 'edit_post.html', {'post': post})


@login_required(login_url='login_view')
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id) 
    if post.user != request.user:
        return redirect('post_list')
    post.delete()
    return redirect('post_list')