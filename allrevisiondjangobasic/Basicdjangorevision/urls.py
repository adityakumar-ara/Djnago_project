from django.contrib import admin
from django.urls import path,include
from .import views 

urlpatterns = [
    path('register/',views.register, name='register'),
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('student/',views.student_registration, name='student_registration'),
    
    path('updatestudent/<int:id>/',views.update_student_form, name='update_student'),
    path('deletestudent/<int:id>/',views.delete_student, name='delete_student'),
]