from django.urls import path
from . import views  # Import your views file

urlpatterns = [
    # This maps 'http://127.0.0.1:8000/send-test-email/' to your view
    path('send-test-email/', views.send_test_email, name='send_test_email'),
]
