from django.urls import path

from apps.orders.api_endpoints.cart import CartDetailAPIView
from apps.orders.api_endpoints.cart_entry import (CartEntryCreateAPIView,
                                                  CartEntryDeleteAPIView,
                                                  CartEntryListAPIView,
                                                  CartEntryUpdateAPIView)

app_name = "orders"

urlpatterns = [
    # cart
    path("carts/<int:user_id>/", CartDetailAPIView.as_view(), name="cart-detail"),
    # cart entries
    path("cart-entries/list/", CartEntryListAPIView.as_view(), name="cart-entry-list"),
    path("cart-entries/create/", CartEntryCreateAPIView.as_view(), name="cart-entry-create"),
    path("cart-entries/<int:pk>/update/", CartEntryUpdateAPIView.as_view(), name="cart-entry-update"),
    path("cart-entries/<int:pk>/delete/", CartEntryDeleteAPIView.as_view(), name="cart-entry-delete"),
]
