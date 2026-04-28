from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    roll = models.CharField(max_length=20 , unique=True)
    village = models.CharField(max_length=100)
    image = models.ImageField(upload_to='studetn/', null=True ,blank=True)
    Email = models.EmailField(unique=True)
    def __str__(self):
        return f"{self.name} - {self.roll} - {self.village} - {self.image} - {self.Email}"