from django.db import models
from django.contrib.auth.models import User

# Create your models here.


from django.contrib.auth.models import User
from django.db import models

class SignUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username    

class Product_list(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.FileField(upload_to='product')
    description = models.TextField()
    quantity = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    


