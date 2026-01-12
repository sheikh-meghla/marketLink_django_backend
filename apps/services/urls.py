from django.urls import path
from .views import (
    ServiceListCreateAPIView,
    ServiceDetailAPIView,
    ServiceVariantListCreateAPIView,
    ServiceVariantDetailAPIView
)

urlpatterns = [
    # Service URLs
    path('services/', ServiceListCreateAPIView.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceDetailAPIView.as_view(), name='service-detail'),

    # ServiceVariant URLs
    path('variants/', ServiceVariantListCreateAPIView.as_view(), name='variant-list-create'),
    path('variants/<int:pk>/', ServiceVariantDetailAPIView.as_view(), name='variant-detail'),
]
