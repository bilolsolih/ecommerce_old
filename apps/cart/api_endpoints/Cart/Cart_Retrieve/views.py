from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import CartRetrieveSerializer
from ....models import Cart
from ....permissions import IsTheOwner


class CartRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsTheOwner]
    queryset = Cart.objects.all()
    serializer_class = CartRetrieveSerializer
    lookup_field = 'user_id'
