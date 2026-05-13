from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StudentRegistration(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['std_name','std_roll','std_village','std_pinCode','department','course','std_email']

        widgets = {
            'std_name': forms.TextInput(attrs={'class': 'form-control'}),
            'std_roll': forms.TextInput(attrs={'class': 'form-control'}),
            'std_village': forms.TextInput(attrs={'class': 'form-control'}),
            'std_pinCode': forms.NumberInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'std_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }



class BasicSignupForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email'] 