from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.orders.models import Cart
from apps.orders.permissions import IsTheOwner
from .serializers import CartRetrieveSerializer


class CartRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsTheOwner]
    queryset = Cart.objects.all()
    serializer_class = CartRetrieveSerializer
    lookup_field = "user_id"


__all__ = ["CartRetrieveAPIView"]
