from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import CheckoutSerializer, OrderSerializer
from .services import checkout


class CheckoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request) -> Response:
        serializer = CheckoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order, created = checkout(customer=request.user, **serializer.validated_data)
        return Response(
            OrderSerializer(order).data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )


class OrderList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.prefetch_related("lines").filter(
            customer=self.request.user
        ).order_by("-created_at")
