import stripe
from django.conf import settings
from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.order_management.serializers import RepairOrderSerializer
from apps.services.models import ServiceVariant
from .models import RepairOrder

# Initialize Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY


class OrderCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        variant_id = request.data.get("variant_id")

        if not variant_id:
            return Response({
                "status": "error",
                "message": "variant_id is required"
            })

        with transaction.atomic():
            try:
                variant = ServiceVariant.objects.select_for_update().get(id=variant_id)
            except ServiceVariant.DoesNotExist:
                return Response({
                    "status": "error",
                    "message": "Service variant not found"
                })

            if variant.stock <= 0:
                return Response({
                    "status": "error",
                    "message": "Out of stock"
                })

            variant.stock -= 1
            variant.save()

            vendor = variant.service.vendor

            order = RepairOrder.objects.create(
                customer=request.user,
                vendor=vendor,
                variant=variant,
                total_amount=variant.price,
                status="pending",
            )

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="payment",
            customer_email=request.user.email,
            line_items=[
                {
                    "price_data": {
                        "currency": "bdt",
                        "unit_amount": int(order.total_amount * 100),
                        "product_data": {
                            "name": f"{variant.service.name} - {variant.name}",
                            "description": variant.service.description,
                        },
                    },
                    "quantity": 1,
                }
            ],
            metadata={
                "order_id": str(order.order_id),
            },
            success_url="https://frontend.test/payment-success",
            cancel_url="https://frontend.test/payment-cancelled",
        )

        return Response({
            "status": "success",
            "message": "Order created successfully",
            "order_id": order.order_id,
            "checkout_url": checkout_session.url,
        })

class MyOrderListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        customer = request.user

        my_orders = RepairOrder.objects.filter(customer=customer).order_by("-created_at")

        serializer = RepairOrderSerializer(my_orders, many=True)

        return Response({
            "status": "success",
            "message": "My orders retrieved successfully",
            "data": serializer.data
        })


@method_decorator(csrf_exempt, name='dispatch')
class StripeWebhookAPIView(APIView):
    permission_classes = []

    def post(self, request):
        payload = request.body
        sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

        print(f"Webhook received - Signature: {sig_header}")
        print(f"Payload length: {len(payload)}")

        if not sig_header:
            print("ERROR: No Stripe signature header found")
            return Response({
                "status": "error",
                "message": "No signature header"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            event = stripe.Webhook.construct_event(
                payload,
                sig_header,
                settings.STRIPE_WEBHOOK_SECRET
            )
            print(f"Webhook event verified: {event['type']}")
        except ValueError as e:
            print(f"ERROR: Invalid payload - {str(e)}")
            return Response({
                "status": "error",
                "message": "Invalid payload"
            }, status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.SignatureVerificationError as e:
            print(f"ERROR: Signature verification failed - {str(e)}")
            return Response({
                "status": "error",
                "message": "Invalid signature"
            }, status=status.HTTP_400_BAD_REQUEST)

       
        if event["type"] == "checkout.session.completed":
            session = event["data"]["object"]

            order_id = session["metadata"].get("order_id")
            amount_total = session["amount_total"] / 100

            print(f"Processing payment for order: {order_id}, amount: {amount_total}")

            try:
                order = RepairOrder.objects.get(order_id=order_id)
            except RepairOrder.DoesNotExist:
                print(f"ERROR: Order {order_id} not found")
                return Response({
                    "status": "error",
                    "message": "Order not found"
                }, status=status.HTTP_404_NOT_FOUND)

            if order.total_amount != amount_total:
                print(f"ERROR: Amount mismatch - Expected: {order.total_amount}, Got: {amount_total}")
                return Response({
                    "status": "error",
                    "message": "Amount mismatch"
                }, status=status.HTTP_400_BAD_REQUEST)

            order.status = "paid"
            order.save(update_fields=["status"])
            print(f"SUCCESS: Order {order_id} marked as paid")


        return Response({
            "status": "success",
            "message": "Webhook processed successfully"
        }, status=status.HTTP_200_OK)

