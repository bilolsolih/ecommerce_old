from rest_framework import serializers

from apps.store.models import Category


class SearchProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "slug",
        ]
