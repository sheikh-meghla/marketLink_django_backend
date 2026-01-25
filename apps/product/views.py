from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer


# --------- Service CRUD ---------
class CategoryCreateAPIView(APIView):

    permission_classes = []

    def post(self, request):

        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "status" : "success",
                "message" : "Category created successfully.",
                "data" : serializer.data
            })
            
        return Response({
            "status" : "error",
            "message" : "Category creation failed.",
            "data" : serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

