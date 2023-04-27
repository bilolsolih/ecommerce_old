from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.orders.models import CartOrderItem
from .permissions import IsTheOwner


class CartItemDestroyAPIView(DestroyAPIView):
    queryset = CartOrderItem.objects.all()
    permission_classes = [IsAuthenticated, IsTheOwner]


__all__ = ["CartItemDestroyAPIView"]
