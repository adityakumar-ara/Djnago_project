from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Branch, Course, CustomeUser, Student


@admin.register(CustomeUser)
class CustomeUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Details', {
            'fields': (
                'full_name', 'mobile_number', 'dob', 'address', 'alternate_mobile_no', 'profile_image', 'gender'
            )
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Details', {
            'fields': (
                'full_name', 'email', 'mobile_number', 'address', 'alternate_mobile_no', 'profile_image', 'gender'
            )
        }),
    )
    list_display = ('username', 'full_name', 'mobile_number', 'gender', 'is_staff')
    search_fields = ('username', 'full_name', 'email', 'mobile_number')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_name')
    search_fields = ('course_name',)


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'branch_name', 'course')
    list_filter = ('course',)
    search_fields = ('branch_name', 'course__course_name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('std_roll', 'std_name', 'course', 'branch', 'semester', 'std_email', 'created_at')
    search_fields = ('std_name', 'std_roll', 'std_email')
    list_filter = ('course', 'branch', 'semester', 'gender')
