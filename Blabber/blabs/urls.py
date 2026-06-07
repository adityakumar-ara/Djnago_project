from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns =[
    path('signup/',views.signup_view, name='signup_view'),
    path('login/',views.login_view, name='login_view'),
    path('', views.post_list, name='post_list'),
    path('create/',views.create_post, name='create_post'),

    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='edit_post'),
]