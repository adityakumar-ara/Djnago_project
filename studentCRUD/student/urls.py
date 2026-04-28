from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
 path('students/',views.show_students, name='students'),
 path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
 path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
] 