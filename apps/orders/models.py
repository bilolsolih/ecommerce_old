from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

# TODO orders model


class Cart(BaseModel):
    user = models.OneToOneField(
        verbose_name=_("Customer"), to="users.User", related_name="cart", on_delete=models.CASCADE
    )
    coupon = models.ForeignKey(
        verbose_name=_("Coupon"),
        to="orders.Coupon",
        related_name="carts",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # entries
    class Meta:
        verbose_name = _("orders")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return f"{self.user.username}'s orders"


class CartEntry(BaseModel):
    cart = models.ForeignKey(verbose_name=_("cart"), to="orders.Cart", related_name="entries", on_delete=models.CASCADE)
    product = models.ForeignKey(
        verbose_name=_("Product name"),
        to="store.Product",
        related_name="cart_entries",
        on_delete=models.SET_NULL,
        null=True,
    )
    delivery_service = models.ForeignKey(
        verbose_name=_("Delivery service"),
        to="services.DeliveryService",
        related_name="entries",
        on_delete=models.SET_NULL,
        null=True,
    )
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"), default=0)

    class Meta:
        verbose_name = _("cart entry")
        verbose_name_plural = _("cart entries")
        unique_together = ("cart", "product")

    def __str__(self):
        return f"cart entry {self.id} with {self.product.title}"


class Coupon(BaseModel):
    users = models.ManyToManyField(
        verbose_name=_("Users who used the coupon"), to="users.User", related_name="coupons", blank=True
    )

    coupon_code = models.CharField(verbose_name=_("Coupon code"), max_length=24)
    discount = models.PositiveIntegerField(verbose_name=_("Coupon discount"), default=0)
    expiry_date = models.DateTimeField(verbose_name=_("Expiry date"), default=timezone.now)
    times_can_be_used = models.PositiveIntegerField(verbose_name=_("Times can be used"), default=1)
    times_used = models.PositiveIntegerField(verbose_name=_("Times used"), default=0)
    is_active = models.BooleanField(verbose_name=_("Is active?"), default=True)

    class Meta:
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")

    def __str__(self):
        return f"Coupon {self.coupon_code}"
