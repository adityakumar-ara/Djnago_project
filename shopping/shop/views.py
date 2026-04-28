from django.shortcuts import render
from .models import Product
def Product_list(request):
    all_product = Product.objects.all()
    data = {
        'Products': all_product
    }
    return render(request,'product_list.html',data)
