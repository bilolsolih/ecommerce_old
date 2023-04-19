from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.orders.models import CartEntry

from .permissions import IsTheOwner
from .serializers import CartEntryListSerializer


class CartEntryListAPIView(ListAPIView):
    queryset = CartEntry.objects.all()
    serializer_class = CartEntryListSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]


__all__ = ["CartEntryListAPIView"]
