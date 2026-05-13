from django.db import models
from django.contrib.auth.models import User

# 1. Department Model
class Department(models.Model):
    name = models.CharField(max_length=50, unique=True) # e.g., 'Computer Science', 'Agriculture'

    def __str__(self):
        return self.name

# 2. Course Model
class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50) # e.g., 'BCA', 'B.Sc Agriculture'

    def __str__(self):
        return f"{self.name} ({self.department.name})"

# 3. Student Model
class Student(models.Model):
    std_name = models.CharField(max_length=100)
    std_roll = models.CharField(max_length=20, unique=True)
    std_village = models.CharField(max_length=100)
    std_pinCode = models.IntegerField()
    std_email = models.EmailField(blank=True, null=True)  # Added email field
    
    # Department aur Course ke liye ForeignKey
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.std_name} - {self.std_roll}"
    
class Student_signup(models.Model):
      student = models.OneToOneField(User, on_delete=models.CASCADE)    
      std_mobile = models.CharField(max_length=10)
      profile_pic = models.ImageField(upload_to='profile/')