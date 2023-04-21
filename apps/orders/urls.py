from django.urls import path

from apps.orders.api_endpoints.Cart.Cart_Retrieve.views import CartRetrieveAPIView
from apps.orders.api_endpoints.CartItem.CartItem_Create.views import CartItemCreateAPIView
from apps.orders.api_endpoints.CartItem.CartItem_Destroy.views import CartItemDestroyAPIView
from apps.orders.api_endpoints.CartItem.CartItem_List.views import CartItemListAPIView

app_name = "orders"

urlpatterns = [
    path("carts/<int:user_id>/", CartRetrieveAPIView.as_view(), name="cart_by_user"),
    path("cart_items/", CartItemListAPIView.as_view(), name="cartItem_list"),
    path("cart_items/create/", CartItemCreateAPIView.as_view(), name="cartItem_create"),
    path("cart_items/destroy/<int:pk>/", CartItemDestroyAPIView.as_view(), name="cartItem_destroy"),
]
