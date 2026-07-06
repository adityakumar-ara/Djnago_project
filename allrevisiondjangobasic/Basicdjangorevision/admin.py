from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomeUser

# Register your models here.
@admin.register(CustomeUser)
class CustomeUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Details', {
            'fields':(
                'full_name','mobile_number','dob','address','alternate_mobile_no','profile_image','gender'
            )
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Details', {
            'fields':(
                'full_name','email','mobile_number','address','alternate_mobile_no','profile_image','gender'
            )
        }),
    )
    list_display = ('username','full_name','mobile_number','gender','is_staff')
    search_fields = ('username','full_name','email','mobile_number')