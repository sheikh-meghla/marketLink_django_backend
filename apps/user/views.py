from .models import VendorProfile
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.validators import ValidationError
from .serializers import (
    SignUpSerializer,
    SignInSerializer,
    SignOutSerializer,
    ChangePasswordSerializer,

    VendorProfileSerializer,
)


# Create your views here.
class SignUpView(APIView):
    permission_classes = []

    def post(self, request):

        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "status" : "success",
                "message" : "User registered successfully.",
                "data" : serializer.data
            })
        raise ValidationError(serializer.errors)

class SignInView(APIView):

    permission_classes = []

    def post(self, request):
        
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                "status" : "success",
                "message" : "User signed in successfully.",
                "data" : serializer.data
            })
        raise ValidationError(serializer.errors)


class SignOutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = SignOutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                "status" : "success",
                "message" : "Sign Out Successfull"
            })
        
        raise ValidationError(serializer.errors)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status" : "success",
                "message" : "Password changed successfully.",
                "data" : serializer.data
            })
        raise ValidationError(serializer.errors)


   




class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def put(self, request):
        user = request.user

        try:
            userProfile = VendorProfile.objects.select_related('user').get(user=user)
        except VendorProfile.DoesNotExist:
            return Response({
                "status" : "error",
                "message" : "User profile not found.",
                "data" : serializer.data
            })

        serializer = VendorProfileSerializer(userProfile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status" : "success",
                "message" : "Profile updated successfully.",
                "data" : serializer.data
            })
        raise ValidationError(serializer.errors)


class ProfileGet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        vendor = request.user

        try:
            profile = VendorProfile.objects.select_related('vendor').get(vendor=vendor)
        except VendorProfile.DoesNotExist:
            return Response({
                "status" : "error",
                "message" : "User profile not found.",
                "data" : serializer.data
            })
        serializer = VendorProfileSerializer(profile)
        return Response({
            "status" : "success",
            "message" : "Profile retrieved successfully.",
            "data" : serializer.data
        })

