from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.orders.models import CartEntry

from .permissions import IsTheOwner
from .serializers import CartEntryListSerializer


class CartEntryListAPIView(ListAPIView):
    serializer_class = CartEntryListSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]

    def get_queryset(self):
        user = self.request.user
        return CartEntry.objects.filter(cart__user=user)


__all__ = ["CartEntryListAPIView"]
