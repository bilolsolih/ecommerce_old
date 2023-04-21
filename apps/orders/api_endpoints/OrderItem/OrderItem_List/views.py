from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from ....models import CartEntry
from .permissions import IsTheOwner
from .serializers import CartEntryListSerializer


class CartEntryListAPIView(ListAPIView):
    queryset = CartEntry.objects.all()
    serializer_class = CartEntryListSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]

    def get_queryset(self):
        user = self.request.user
        self.queryset = self.queryset.filter(cart=user.cart)


__all__ = ["CartEntryListAPIView"]
