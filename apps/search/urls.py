from django.urls import path

from .views import SearchProductAPIView, SearchProductCategoryAPIView

app_name = "search"

urlpatterns = [
    path("categories/<str:query>/", SearchProductCategoryAPIView.as_view()),
    path("products/<str:query>/", SearchProductAPIView.as_view()),
]
