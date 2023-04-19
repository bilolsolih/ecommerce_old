from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated

from .permissions import IsTheOwner
from .serializers import CartEntryUpdateSerializer
from ....models import CartEntry


class CartEntryUpdateAPIView(UpdateAPIView):
    queryset = CartEntry.objects.all()
    serializer_class = CartEntryUpdateSerializer
    permission_classes = [IsAuthenticated, IsTheOwner]
    parser_classes = [FormParser]
