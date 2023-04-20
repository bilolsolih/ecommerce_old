from django_filters import rest_framework as filters

from apps.store.models import Product


class ProductFilter(filters.FilterSet):
    brand = filters.CharFilter(field_name="brand", method="filter_by_brands")

    class Meta:
        model = Product
        fields = ["brand", "condition"]

    def filter_by_brands(self, queryset, name, value):
        brands = value.split(",")
        return queryset.filter(brand__in=brands)
