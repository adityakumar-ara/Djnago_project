from django.db import models
from django.core.validators import RegexValidator

class Product(models.Model):
    
    f_name = models.CharField(max_length=30)
    
    f_adha = models.CharField(
        max_length=12,
        validators=[RegexValidator(r'^\d{12}$', 'Aadhar number must be exactly 12 digits.')],
        null=False
    )
    
    f_vill = models.CharField(max_length=100, null=False)            
    
    f_pin = models.CharField(
        max_length=6,
        validators=[RegexValidator(r'^\d{6}$', 'PIN code must be exactly 6 digits.')],
        null=False
    )

    def __str__(self):
        return self.f_name

class CropSale(models.Model):
    farmer = models.ForeignKey(Product, on_delete=models.CASCADE)    

    CROP_CHOICES = [
        ('Sugarcane', 'Ganna (Sugarcane)'),
        ('Wheat', 'Gehu (Wheat)'),
        ('Rice', 'Dhan (Rice)'),
        ('Maize', 'Makka (Maize)'),
        ('Other', 'Anya (Other)'),
    ]
    crop_name = models.CharField(max_length=50, choices=CROP_CHOICES)
    quantity = models.DecimalField(max_digits=7, decimal_places=2)
    
    UNIT_CHOICES = [
        ('KG', 'Kilogram'),
        ('QTL', 'Quintal'),
        ('TON', 'Ton'),
    ]
    unit = models.CharField(max_length=5, choices=UNIT_CHOICES, default='QTL')

    def __str__(self):
       
        return f"{self.farmer.f_name} - {self.crop_name} ({self.quantity} {self.unit})"