from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('like/<int:id>/', views.like_post, name='like_post'),
    path('reels/', views.reels_view, name='reels'),
]