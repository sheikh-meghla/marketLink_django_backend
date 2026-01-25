from django.contrib import admin
from .models import Product, ProductCategory
from unfold.admin import ModelAdmin, TabularInline

@admin.register(ProductCategory)
class ProductCategoryAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
@admin.register(Product)

class ProductAdmin(ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

