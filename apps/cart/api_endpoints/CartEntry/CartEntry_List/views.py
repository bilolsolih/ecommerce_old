from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsTheOwner
from .serializers import CartEntryListSerializer
from ....models import CartEntry


class CartEntryListAPIView(ListAPIView):
    queryset = CartEntry.objects.all()
    serializer_class = CartEntryListSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]
