from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class CustomeUser(AbstractUser):
    GENDER_CHOICES = (
        ('MALE', 'male'),
        ('FEMALE', 'female'),
        ('OTHER', 'other'),
    ) 
    full_name = models.CharField(max_length=50, null=True,blank= True)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10, unique=True, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    alternate_mobile_no = models.CharField(max_length=10, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image/',blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    
    def __str__(self):
        return self.full_name or self.username 
    
class Student(models.Model):
    user = models.OneToOneField(
        CustomeUser,
        on_delete=models.CASCADE
    )
    GENDER_CHOICES = (
        ('MALE','male'),
        ('FEMALE','female'),
        ('OTHER','other'),
    )
    std_name = models.CharField(max_length=50, null=True, blank=True)
    course = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    semester = models.IntegerField()
    std_roll = models.CharField(max_length=12,null=True,blank=True, unique=True)
    std_no = models.CharField(max_length=10,null=True,blank=True,unique=True)
    std_email = models.EmailField(unique=True, null=True, blank=True)
    std_address = models.TextField(blank=True,null=True)
    std_dob = models.DateField()
    std_image = models.ImageField(upload_to='student/', blank=True, null=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,null=True,blank=True)
    
    def __str__(self):
        return self.std_roll    