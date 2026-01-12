from rest_framework import serializers

from apps.user.serializers import CustomUserSerializer
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


class GetAllServiceSerializer(serializers.ModelSerializer):
    vendor = CustomUserSerializer()
    class Meta:
        model = Service
        fields = ['id','name', 'description', 'variants','vendor']


class GetAllServiceVariantSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    class Meta:
        model = ServiceVariant
        fields = ['id', 'service', 'name', 'price', 'estimated_minutes', 'stock']