from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.create_student, name='add_show'),
    path('show/',views.show_student ,name="show_student"),
    path('signup/',views.student_signup, name='signup'),
]