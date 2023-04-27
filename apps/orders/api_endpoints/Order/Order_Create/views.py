from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.orders.models import Order
from .serializers import OrderCreateSerializer


class OrderCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vd = serializer.validated_data
        new_order = Order.objects.create(
            user=request.user,
            postal_code=vd['postal_code'],
            country=vd['country'],
            region=vd['region'],
            city=vd['city'],
            street=vd['street'],
            coupon=request.user.cart.coupon
        )
        new_order.save()
        items = request.user.cart.items.all()
        for item in items:
            item.cart = None
            item.order = new_order



        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


__all__ = ["OrderCreateAPIView"]
