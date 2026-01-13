from django.urls import path

from .views import (
    OrderCreateAPIView,
    StripeWebhookAPIView,
    MyOrderListAPIView
)

urlpatterns = [
    path("create-order/", OrderCreateAPIView.as_view()),
    path("my-order-list/", MyOrderListAPIView.as_view()),




    # stripe webhook
    path("stripe-webhook/", StripeWebhookAPIView.as_view()),
]