from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated

from apps.orders.models import CartOrderItem

from .permissions import IsTheOwner
from .serializers import CartItemUpdateSerializer


class CartItemUpdateAPIView(UpdateAPIView):
    queryset = CartOrderItem.objects.all()
    serializer_class = CartItemUpdateSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]
    parser_classes = [FormParser]


__all__ = ["CartItemUpdateAPIView"]
