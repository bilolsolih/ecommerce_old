from django.urls import path
from .api_endpoints.Cart.Cart_List.views import CartListAPIView

app_name = 'cart'

urlpatterns = [
    path('carts/', CartListAPIView.as_view(), name='cart_list'),
]
