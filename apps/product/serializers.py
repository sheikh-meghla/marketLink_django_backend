from rest_framework import  serializers

from apps.product.models import ProductCategory
from apps.services.serializers import ServiceVariantSerializer

class CategorySerializer(serializers.ModelSerializer):
    

    class Meta:
        model = ProductCategory
        fields = '__all__'

   