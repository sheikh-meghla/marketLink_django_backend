from rest_framework import serializers
from .models import Service, ServiceVariant

class ServiceVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceVariant
        fields = ['id', 'service', 'name', 'price', 'estimated_minutes', 'stock']

class ServiceSerializer(serializers.ModelSerializer):
    variants = ServiceVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'variants']
