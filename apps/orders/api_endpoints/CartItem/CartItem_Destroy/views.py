from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.orders.models import CartItem
from .permissions import IsTheOwner


class CartItemDestroyAPIView(DestroyAPIView):
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated, IsTheOwner]


__all__ = ["CartItemDestroyAPIView"]