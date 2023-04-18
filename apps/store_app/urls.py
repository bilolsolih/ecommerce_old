from django.urls import path

from .api_endpoints.Brand.Brand_List.views import BrandListAPIView
from .api_endpoints.Category.Category_List.views import CategoryListAPIView
from .api_endpoints.Category.Category_Retrieve.views import CategoryRetrieveAPIView
from .api_endpoints.Product.Product_List.views import ProductListAPIView
from .api_endpoints.Product.Product_Retrieve.views import ProductRetrieveAPIView

app_name = 'store'

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_detail'),
    path('brands/', BrandListAPIView.as_view(), name='brand_list'),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_detail'),

]
