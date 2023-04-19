from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsTheOwner
from .serializers import CartEntryRetrieveSerializer
from ....models import CartEntry


class CartEntryCreateAPIView(RetrieveAPIView):
    queryset = CartEntry.objects.all()
    serializer_class = CartEntryRetrieveSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]
