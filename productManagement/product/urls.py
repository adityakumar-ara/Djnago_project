from django.urls import path
from . import views
urlpatterns =[
    path('',views.product_list, name='product_list'),
    path('add/',views.add, name='add'),
    path('signup/', views.signup_view, name='signup'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('login/',views.login, name='login'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]