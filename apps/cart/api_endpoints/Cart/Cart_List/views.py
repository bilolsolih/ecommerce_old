from rest_framework.generics import ListAPIView

from .serializers import CartListSerializer
from ....models import Cart


class CartListAPIView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer
