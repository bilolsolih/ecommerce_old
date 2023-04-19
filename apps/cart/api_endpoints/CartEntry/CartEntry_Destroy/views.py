from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsTheOwner
from ....models import CartEntry


class CartEntryDestroyAPIView(DestroyAPIView):
    queryset = CartEntry.objects.all()
    permission_classes = [IsAuthenticated, IsTheOwner]
