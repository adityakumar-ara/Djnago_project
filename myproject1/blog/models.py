from django.db import models

# Create your models here.
# from django.db import models

class student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    course = models.CharField(max_length=50, default="BCA") 
    location = models.CharField(max_length=100, default="Meerut")
    profile_pic = models.ImageField(upload_to='students/', null=True, blank=True)

    def __str__(self):
        return self.name