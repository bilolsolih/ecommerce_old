from django.contrib import admin

from apps.store.models import Brand, Category, DealAndOffer, Item, Subcategory


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price_per_unit", "condition"]


admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ProductAdmin)
admin.site.register(Brand)
admin.site.register(DealAndOffer)
