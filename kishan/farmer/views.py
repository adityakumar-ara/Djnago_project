from django.shortcuts import render,redirect

# Create your views here.
from .models import Product,CropSale
#show
def Product_list(request):
    farmer = Product.objects.all()
    sales = CropSale.objects.all()
    contex={
        'farmer':farmer,
        'sales':sales
    }
    return render(request ,'farmer/kishanprod.html',contex)
# add
def register_farmer(request):
    if request.method == "POST":
        # Form se saara data nikalo
        name_data = request.POST.get('f_name')
        aadhar_data = request.POST.get('f_adha')
        village_data = request.POST.get('f_vill')
        pincode_data = request.POST.get('f_pin')
        
        crop_data = request.POST.get('crop_name')
        qty_data = request.POST.get('quantity')
        unit_data = request.POST.get('unit')
        
        # Pehle Kisan ko save karo
        new_farmer = Product.objects.create(
            f_name=name_data,
            f_adha=aadhar_data,
            f_vill=village_data,
            f_pin=pincode_data
        )
        
        # Fir Fasal ko save karo (Kisan se link karke)
        CropSale.objects.create(
            farmer=new_farmer,
            crop_name=crop_data,
            quantity=qty_data,
            unit=unit_data
        )
        
        # Save hone ke baad wapas dashboard par bhej do
        return redirect('Product_list')
        
    # GET Request: Model se choices uthao aur HTML ko bhejo
    context = {
        'crop_choices': CropSale.CROP_CHOICES,
        'unit_choices': CropSale.UNIT_CHOICES
    }
    return render(request, 'farmer/additem.html', context)

# delete
def delete_farmer(request,id):
    farmer = Product.objects.get(id=id)
    farmer.delete()
    return redirect('Product_list')
#edit
def editdetail(request,id):
    farmer = Product.objects.get(id = id)
    crop = CropSale.objects.get(farmer = farmer)
    if request.method == 'POST':
        farmer.f_name =request.POST.get('f_name')
        farmer.f_adha=request.POST.get('f_adha')
        farmer.f_vill = request.POST.get('f_vill')
        farmer.f_pin = request.POST.get('f_pin')
        farmer.save()

        crop.crop_name = request.POST.get('crop_name')
        crop.quantity = request.POST.get('quantity')
        crop.unit = request.POST.get('unit')
        crop.save()

        return redirect(Product_list)
    
    context = {
        'farmer': farmer,
        'crop': crop,
        'crop_choices': CropSale.CROP_CHOICES,
        'unit_choices': CropSale.UNIT_CHOICES
    }
    
    return render(request, 'farmer/farmeredit.html', context)