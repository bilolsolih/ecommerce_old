from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from ....models import CartItem
from .permissions import IsTheOwner
from .serializers import CartItemListSerializer


class CartItemListAPIView(ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemListSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]

    def get_queryset(self):
        user = self.request.user
        self.queryset = self.queryset.filter(cart=user.cart)


__all__ = ["CartItemListAPIView"]
