from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import RepairOrder


@admin.register(RepairOrder)
class RepairOrderAdmin(ModelAdmin):
    list_display = (
        "order_id",
        "customer",
        "vendor",
        "variant",
        "status",
        "total_amount",
        "created_at",
    )
    search_fields = (
        "order_id",
        "customer__username",
        "vendor__username",
        "variant__name",
        "status",
    )
    
    list_filter = (
        "status",
        "created_at",
    )


    
    
    