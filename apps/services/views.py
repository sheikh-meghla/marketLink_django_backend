from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Service, ServiceVariant
from .serializers import ServiceSerializer, ServiceVariantSerializer, GetAllServiceSerializer,GetAllServiceVariantSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated

# --------- Service CRUD ---------
class ServiceListCreateAPIView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def get(self, request):

        user = request.user
        services = Service.objects.filter(vendor = user)

        serializer = ServiceSerializer(services,  many=True)
        return Response({
            "status" : "success",
            "message" : "Service retrieved successfully.",
            "data" : serializer.data
        })

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(vendor=request.user)
            return Response({
                "status" : "success",
                "message" : "Service created successfully.",
                "data" : serializer.data
            })
            
        return Response({
            "status" : "error",
            "message" : "Service creation failed.",
            "data" : serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)



class ServiceDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, pk):
        service = Service.objects.filter(vendor = request.user, id = pk).first()
        serializer = ServiceSerializer(service)
        return Response({
            "status": "success",
            "message": "Service retrieved successfully.",
            "data": serializer.data
        })

    def put(self, request, pk):
        user = request.user
        service = Service.objects.filter(vendor = user, id = pk).first() 
        
        serializer = ServiceSerializer(service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Service updated successfully.",
                "data": serializer.data
            })

        return Response({
            "status": "error",
            "message": "Service update failed.",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = request.user
        service = Service.objects.filter(vendor = user, id = pk).first() 

        if not service:
            return Response({
                "status": "error",
                "message": "Service not found.",
            }, status=status.HTTP_404_NOT_FOUND)
            
        service.delete()
        return Response({
            "status": "success",
            "message": "Service deleted successfully.",
        })

# --------- ServiceVariant CRUD ---------
class ServiceVariantListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        variants = ServiceVariant.objects.filter(service__vendor = user)
        
        serializer = ServiceVariantSerializer(variants, many=True)
        
        return Response({
            "status": "success",
            "message": "Service variants retrieved successfully.",
            "data": serializer.data
        })

    def post(self, request):
        serializer = ServiceVariantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "status": "success",
                "message": "Service variant created successfully.",
                "data": serializer.data
            })

        return Response({
            "status": "error",
            "message": "Service variant creation failed.",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class ServiceVariantDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request, pk):
        user = request.user
        variant = ServiceVariant.objects.filter(service__vendor = user, id = pk).first()    
        
        serializer = ServiceVariantSerializer(variant)
        return Response({
            "status": "success",
            "message": "Service variant retrieved successfully.",
            "data": serializer.data
        })

    def put(self, request, pk):
        user = request.user
        variant = ServiceVariant.objects.filter(service__vendor = user, id = pk).first()    
        
        serializer = ServiceVariantSerializer(variant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response({
                "status": "success",
                "message": "Service variant updated successfully.",
                "data": serializer.data
            })

        return Response({
            "status": "error",
            "message": "Service variant update failed.",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = request.user
        variant = ServiceVariant.objects.filter(service__vendor = user, id = pk).first()  

        if not variant:
            return Response({
                "status": "error",
                "message": "Service variant not found.",
            }, status=status.HTTP_404_NOT_FOUND)
              
        variant.delete()
        return Response({
            "status": "success",
            "message": "Service variant deleted successfully.",
        })
    

# public API for customer

class AllServiceApiView(APIView):
    permission_classes = []

    def get(self, request):

        services = Service.objects.select_related('vendor').all()

        serializer = GetAllServiceSerializer(services, many=True)
        return Response({
            "status" : "success",
            "message" : "Services retrieved successfully.",
            "data" : serializer.data
        })

class AllVariantApiView(APIView):
    permission_classes = []

    def get(self, request):

        variants = ServiceVariant.objects.select_related('service').all()

        serializer = GetAllServiceVariantSerializer(variants, many=True)

        return Response({
            "status" : "success",
            "message" : "Service variants retrieved successfully.",
            "data" : serializer.data
        })

