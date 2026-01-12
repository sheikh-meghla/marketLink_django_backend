from django.contrib import admin
from .models import Service, ServiceVariant
from unfold.admin import ModelAdmin, TabularInline
# Inline for ServiceVariant
class ServiceVariantInline(TabularInline):
    model = ServiceVariant
    extra = 3
    can_delete = True

# Service admin with inline variants
@admin.register(Service)
class ServiceAdmin(ModelAdmin):  # ModelAdmin Django-এর
    list_display = ('name', 'vendor',)
    search_fields = ('name', 'vendor__business_name',)
    list_filter = ('vendor',)
    inlines = [ServiceVariantInline]

# Optional: separate admin for ServiceVariant
@admin.register(ServiceVariant)
class ServiceVariantAdmin(ModelAdmin):  # ModelAdmin Django-এর
    list_display = ('name', 'service', 'price', 'estimated_minutes', 'stock')
    search_fields = ('name', 'service__name', 'service__vendor__business_name')
    list_filter = ('service__vendor',)
