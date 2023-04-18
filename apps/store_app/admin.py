from django.contrib import admin

from apps.store_app.models import Category, Subcategory, Product, Brand, DealAndOffer, PriceRange, ProductPhoto


class PriceRangeInline(admin.StackedInline):
    model = PriceRange


class ProductPhotoInline(admin.StackedInline):
    model = ProductPhoto


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['sold_quantity']
    inlines = [PriceRangeInline, ProductPhotoInline]


admin.site.register(PriceRange)
admin.site.register(Subcategory)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(DealAndOffer)
