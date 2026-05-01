from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment,Like
from django.core.exceptions import ValidationError

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        text = request.POST.get('text')
        
        name = request.POST.get('name')
        if not name:
            if request.user.is_authenticated:
                name = request.user.username
            else:
                name = "Anonymous"

        Comment.objects.create(
            post=post,
            user=request.user if request.user.is_authenticated else None,
            name=name, 
            text=text
        )
        # After saving the comment, redirect back
        return redirect('post_detail', id=id)

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments
    })

@login_required



def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        post = Post(
            title=title,
            content=content,
            image=image,
            video=video,
            author=request.user
        )

        try:
            post.full_clean()  
            post.save()         
            return redirect('post_list')

        except ValidationError as e:
            return render(request, 'create.html', {
                'error': e.message_dict
            })

    return render(request, 'create_post.html')


@login_required
def like_post(request, id):
    post = Post.objects.get(id=id)
    
    like, created = Like.objects.get_or_create(
        post=post,
        user=request.user
    )

    if not created:
        like.delete() 

    return redirect('post_detail', id=id)

def reels_view(request):
    posts = Post.objects.all()
    return render(request, 'reels.html', {'posts': posts})    