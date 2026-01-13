import uuid
from django.db import models
from apps.services.models import ServiceVariant
from apps.user.models import CustomUser



class RepairOrder(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("failed", "Failed"),
        ("cancelled", "Cancelled"),
    )

    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='customer_orders')
    vendor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='vendor_orders')
    variant = models.ForeignKey(ServiceVariant, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PaymentEvent(models.Model):
    event_id = models.CharField(max_length=255, unique=True)
    order = models.ForeignKey('RepairOrder', on_delete=models.CASCADE)
    processed_at = models.DateTimeField(auto_now_add=True)





