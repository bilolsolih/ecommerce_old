from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.orders.models import CartEntry
from .permissions import IsTheOwner


class CartEntryDestroyAPIView(DestroyAPIView):
    queryset = CartEntry.objects.all()
    permission_classes = [IsAuthenticated, IsTheOwner]


__all__ = ["CartEntryDestroyAPIView"]
