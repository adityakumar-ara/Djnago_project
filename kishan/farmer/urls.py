from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns =[
    path('farmer/',views.Product_list, name='Product_list'),
    path('register/', views.register_farmer, name='register'),
    # farmer/urls.py
    path('delete/<int:id>/', views.delete_farmer, name='delete_farmer'),
    # Edit
    path('edit/<int:id>/',views.editdetail, name='editdetail')
]