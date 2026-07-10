from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomeUser(AbstractUser):
    GENDER_CHOICES = (
        ('MALE', 'male'),
        ('FEMALE', 'female'),
        ('OTHER', 'other'),
    )
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10, unique=True, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    alternate_mobile_no = models.CharField(max_length=10, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image/', blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)

    def __str__(self):
        return self.full_name or self.username


class Course(models.Model):
    course_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.course_name


class Branch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branches')
    branch_name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('course', 'branch_name')

    def __str__(self):
        return f"{self.branch_name} ({self.course.course_name})"


class Student(models.Model):
    GENDER_CHOICES = (
        ('MALE', 'male'),
        ('FEMALE', 'female'),
        ('OTHER', 'other'),
    )

    user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE, null=True, blank=True)
    std_name = models.CharField(max_length=50, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='students')
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, related_name='students')
    semester = models.PositiveIntegerField()
    std_roll = models.CharField(max_length=12, null=True, blank=True, unique=True)
    std_no = models.CharField(max_length=10, null=True, blank=True, unique=True)
    std_email = models.EmailField(unique=True, null=True, blank=True)
    std_address = models.TextField(blank=True, null=True)
    std_dob = models.DateField()
    std_image = models.ImageField(upload_to='student/', blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.std_name or self.std_roll or str(self.id)
