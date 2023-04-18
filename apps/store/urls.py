from django.urls import path

from .api_endpoints.Brand.Brand_List.views import BrandListAPIView
from .api_endpoints.Brand.Brand_Retrieve.views import BrandRetrieveAPIView
from .api_endpoints.Category.Category_List.views import CategoryListAPIView
from .api_endpoints.Category.Category_Retrieve.views import CategoryRetrieveAPIView
from .api_endpoints.Product.Product_List.views import ProductListAPIView
from .api_endpoints.Product.Product_Retrieve.views import ProductRetrieveAPIView
from .api_endpoints.Subcategory.Subcategory_List.views import SubcategoryListAPIView
from .api_endpoints.Subcategory.Subcategory_Retrieve.views import SubcategoryRetrieveAPIView

app_name = 'store'

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_detail'),
    path('subcategories/', SubcategoryListAPIView.as_view(), name='subcategory_list'),
    path('subcategories/<int:pk>/', SubcategoryRetrieveAPIView.as_view(), name='subcategory_detail'),
    path('brands/', BrandListAPIView.as_view(), name='brand_list'),
    path('brands/<int:pk>/', BrandRetrieveAPIView.as_view(), name='brand_detail'),

]
