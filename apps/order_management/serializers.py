from rest_framework import  serializers
from .models import RepairOrder
from apps.services.serializers import ServiceVariantSerializer
class RepairOrderSerializer(serializers.ModelSerializer):
    variant = ServiceVariantSerializer(read_only=True)
    customer_email = serializers.EmailField(source="customer.email", read_only=True)
    vendor_email = serializers.EmailField(source="vendor.email", read_only=True)

    class Meta:
        model = RepairOrder
        fields = [
            "order_id",
            "customer_email",
            "vendor_email",
            "variant",
            "status",
            "total_amount",
            "created_at",
            "updated_at",
        ]

   