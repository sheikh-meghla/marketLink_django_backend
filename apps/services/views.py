from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Service, ServiceVariant
from .serializers import ServiceSerializer, ServiceVariantSerializer
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated

# --------- Service CRUD ---------
class ServiceListCreateAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        services = Service.objects.all()

        serializer = ServiceSerializer(services,  many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(vendor=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ServiceDetailAPIView(APIView):


    def get(self, request, pk):

        service = Service.objects.filter(id = pk)

        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        service = self.get_object(pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------- ServiceVariant CRUD ---------
class ServiceVariantListCreateAPIView(APIView):
    def get(self, request):
        variants = ServiceVariant.objects.all()
        serializer = ServiceVariantSerializer(variants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceVariantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceVariantDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(ServiceVariant, pk=pk)

    def get(self, request, pk):
        variant = self.get_object(pk)
        serializer = ServiceVariantSerializer(variant)
        return Response(serializer.data)

    def put(self, request, pk):
        variant = self.get_object(pk)
        serializer = ServiceVariantSerializer(variant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        variant = self.get_object(pk)
        variant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
