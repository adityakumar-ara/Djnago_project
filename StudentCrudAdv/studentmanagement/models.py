from django.db import models

# Create your models here.
class studetn(models.Model):
    name = models.CharField(max_length=40)
    e_no = models.CharField(max_length=12, null=True, blank=True)
    image= models.ImageField(upload_to='studetn', null=True, blank=True)
    def __str__(self):
        return self.name
    