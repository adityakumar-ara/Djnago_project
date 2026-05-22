from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse # Or standard exceptions depending on where you use this

def send_test_email(request):
    """Send a test email using the SMTP credentials configured in settings."""
    
    subject = 'Inventory Management Test Email'
    message = 'This is a test email sent from Django using the configured SMTP settings.'
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_RECEIPT_ADDRESS]

    try:
        
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False
        )

        return HttpResponse(
            f'Test email sent successfully to {settings.EMAIL_RECEIPT_ADDRESS}'
        )

    except Exception as exc:
        return HttpResponse(
            f'Error sending test email: {exc}',
            status=500
        )