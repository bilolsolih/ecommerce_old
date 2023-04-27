from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from ....models import CartOrderItem
from .permissions import IsTheOwner
from .serializers import CartItemListSerializer


class CartItemListAPIView(ListAPIView):
    queryset = CartOrderItem.objects.all()
    serializer_class = CartItemListSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]

    def get_queryset(self):
        user = self.request.user
        self.queryset = self.queryset.filter(cart=user.cart)


__all__ = ["CartItemListAPIView"]
