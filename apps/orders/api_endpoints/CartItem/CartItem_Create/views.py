from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.orders.models import Cart, CartItem

from .serializers import CartItemCreateSerializer


class CartItemCreateAPIView(CreateAPIView):
    pass


__all__ = ["CartItemCreateAPIView"]
