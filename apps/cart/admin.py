from django.contrib import admin

from .models import Cart, CartOrderItem, Coupon, Order, OrderItem

admin.site.register(CartOrderItem)
admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(OrderItem)


class CartEntryInline(admin.StackedInline):
    model = CartOrderItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartEntryInline]

# Register your models here.
