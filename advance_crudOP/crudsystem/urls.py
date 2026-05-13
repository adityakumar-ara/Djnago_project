from django.urls import path,include
from .import views
urlpatterns = [
    path('create/',views.create_student, name='add_show'),
    path('',views.show_student ,name="show_student"),
    path('signup/',views.student_signup, name='signup'),
    path('send-test-email/',views.send_user_email, name='send_user_email'),
]