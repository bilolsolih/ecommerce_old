from django.urls import path

from .api_endpoints.Cart.Cart_Retrieve.views import CartRetrieveAPIView
from .api_endpoints.CartEntry.CartEntry_Create.views import CartEntryCreateAPIView

app_name = 'cart'

urlpatterns = [
    path('carts/<int:user_id>/', CartRetrieveAPIView.as_view(), name='cart_by_user'),
    path('cart_entries/create/', CartEntryCreateAPIView.as_view(), name='cartentry_create'),
]
