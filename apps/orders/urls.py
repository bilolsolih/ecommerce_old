from django.urls import path

from apps.orders.api_endpoints.cart import CartDetailAPIView
from apps.orders.api_endpoints.cart_entry import CartEntryCreateAPIView

app_name = "orders"

urlpatterns = [
    path("carts/<int:user_id>/", CartDetailAPIView.as_view(), name="cart_by_user"),
    path("cart_entries/create/", CartEntryCreateAPIView.as_view(), name="cartentry_create"),
]
