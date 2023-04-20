from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated

from apps.orders.models import CartEntry

from .permissions import IsTheOwner
from .serializers import CartEntryUpdateSerializer


class CartEntryUpdateAPIView(UpdateAPIView):
    queryset = CartEntry.objects.all()
    serializer_class = CartEntryUpdateSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]
    parser_classes = [FormParser]


__all__ = ["CartEntryUpdateAPIView"]
