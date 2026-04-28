from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_price = models.DecimalField(max_digits=12 ,decimal_places=2)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='Product/', null=True, blank=True)
    def __str__(self):
        return f"{self.product_name}"   
