from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import CustomUser, VendorProfile
from django.utils.html import format_html
@admin.register(CustomUser)
class CustomAdminClass(ModelAdmin):
      list_display = ('id', 'email', 'role')
    

@admin.register(VendorProfile)
class VendorProfileAdmin(ModelAdmin):
    list_display = ('id', 'vendor', 'business_name', 'address', 'is_active')
