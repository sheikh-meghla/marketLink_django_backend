from django.db import models
from apps.user.models import CustomUser

class Service(models.Model):
    vendor = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='vendor_service' )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ServiceVariant(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='variants')
    name = models.CharField(max_length=50)  # e.g., Basic, Premium
    price = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_minutes = models.IntegerField()
    stock = models.PositiveIntegerField(default=1)  # concurrent booking limit

    def __str__(self):
        return self.name
