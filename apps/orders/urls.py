from django.urls import path

from apps.orders.api_endpoints.Cart.Cart_Retrieve.views import CartRetrieveAPIView
from apps.orders.api_endpoints.CartEntry.CartEntry_Create.views import CartEntryCreateAPIView
from apps.orders.api_endpoints.CartEntry.CartEntry_Destroy.views import CartEntryDestroyAPIView
from apps.orders.api_endpoints.CartEntry.CartEntry_List.views import CartEntryListAPIView

app_name = "orders"

urlpatterns = [
    path("carts/<int:user_id>/", CartRetrieveAPIView.as_view(), name="cart_by_user"),
    path('cart_entries/', CartEntryListAPIView.as_view(), name='cartentry_list'),
    path("cart_entries/create/", CartEntryCreateAPIView.as_view(), name="cartentry_create"),
    path('cart_entries/destroy/<int:pk>/', CartEntryDestroyAPIView.as_view(), name='cartentry_destroy'),

]
