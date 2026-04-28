# Create your models here.

from django.db import models

class Student(models.Model):
    std_name = models.CharField(max_length=100)
    std_roll = models.IntegerField()
    std_image = models.ImageField(upload_to='student_images/')
    std_email = models.EmailField()
    std_city = models.CharField(max_length=100)

    def __str__(self):
        return self.std_name
