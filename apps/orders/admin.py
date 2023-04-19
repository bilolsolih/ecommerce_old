from django.contrib import admin

from .models import Cart, CartEntry, Coupon

admin.site.register(CartEntry)
admin.site.register(Coupon)


class CartEntryInline(admin.StackedInline):
    model = CartEntry


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartEntryInline]


# Register your models here.