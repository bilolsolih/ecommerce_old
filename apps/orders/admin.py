from django.contrib import admin

from .models import Cart, CartItem, Coupon

admin.site.register(CartItem)
admin.site.register(Coupon)


class CartEntryInline(admin.StackedInline):
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartEntryInline]

# Register your models here.
