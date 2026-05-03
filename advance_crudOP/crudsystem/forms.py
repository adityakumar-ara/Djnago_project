from django import forms
from .models import Student
from django.contrib.auth.models import User
from .models import Student_signup


class StudentRegistration(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['std_name','std_roll','std_village','std_pinCode','department','course']

        widgets = {
            'std_name': forms.TextInput(attrs={'class': 'form-control'}),
            'std_roll': forms.TextInput(attrs={'class': 'form-control'}),
            'std_village': forms.TextInput(attrs={'class': 'form-control'}),
            'std_pinCode': forms.NumberInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
        }

class student_signup(forms.ModelForm):
    class Meta:
        model = Student_signup
        fields = '__all__'
