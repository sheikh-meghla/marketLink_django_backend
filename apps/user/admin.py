from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import CustomUser, VendorProfile
from django.utils.html import format_html
from django.contrib.auth.models import Group, Permission


# @admin.register(Group)
# class GroupAdminClass(ModelAdmin):
#      list_display = ('id','name')

@admin.register(Permission)
class Permission(ModelAdmin):
     list_display = ('id','name')

@admin.register(CustomUser)
class CustomAdminClass(ModelAdmin):
      list_display = ('id', 'email', 'role')
      list_display_links = ('id', 'email', 'role')
      fieldsets = (
        ('User Info', {
            'fields': ('email', 'role', 'password',),
        }),


         ('Permissions', {
            'fields': ('is_staff', 'groups',),
        }),
    )
    

@admin.register(VendorProfile)
class VendorProfileAdmin(ModelAdmin):
    list_display = ('id', 'vendor', 'business_name', 'address', 'is_active')
