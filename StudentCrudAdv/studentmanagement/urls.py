from django.urls import path,include
from .import views
urlpatterns =[
    path('', views.show_student, name='show_student'),
    path('addstudent/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student, name= 'edit_student'),
    path('delete/<int:id>/', views.delete_student , name='delete_student'),
]
