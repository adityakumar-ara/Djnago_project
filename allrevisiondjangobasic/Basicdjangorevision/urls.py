from django.contrib import admin
from django.urls import path,include
from .import views 

urlpatterns = [
    path('register/',views.register, name='register'),
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
]