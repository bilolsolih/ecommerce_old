from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.orders.models import Cart, CartItem

from .serializers import CartItemCreateSerializer


class CartItemCreateAPIView(CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            vd = serializer.validated_data
            cart = Cart.objects.get_or_create(user=request.user)
            product = vd["the_product"]
            delivery_service = vd["delivery_service"]
            quantity = vd["quantity"]
            entry = CartItem.objects.create(
                cart=cart[0], product=product, delivery_service=delivery_service, quantity=quantity
            )
            entry.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


__all__ = ["CartItemCreateAPIView"]
