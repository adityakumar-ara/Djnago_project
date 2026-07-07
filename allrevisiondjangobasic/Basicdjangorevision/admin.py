from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
@admin.register(CustomeUser)
class CustomeUserAdmin(UserAdmin):
    # Admin jab existing user edit karega, to ye extra fields bhi dikhenge.
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Details', {
            'fields':(
                'full_name','mobile_number','dob','address','alternate_mobile_no','profile_image','gender'
            )
        }),
    )
    # Admin jab naya user banayega, tab ye fields bhi form me dikhenge.
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Details', {
            'fields':(
                'full_name','email','mobile_number','address','alternate_mobile_no','profile_image','gender'
            )
        }),
    )
    # Admin panel ki list me ye columns dikhengi.
    list_display = ('username','full_name','mobile_number','gender','is_staff')
    # Admin panel ke search box se in fields par search kar sakte ho.
    search_fields = ('username','full_name','email','mobile_number')
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Personal Detail",{
            "fields":(
                'std_name',
                'std_gender',
                'std_image',
            )
        }),
        ("Acardmic Detail",{
            "fields":(
                'std_roll',
                'course',
                'branch',
                'semester',
            )
        }),
        ("Contact Detail",{
            "fields":(
                'std_no',
                'std_email',
                'std_address',
            )
        })
    )    