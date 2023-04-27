from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Cart(BaseModel):
    user = models.OneToOneField(verbose_name=_("The owner of the cart"), to="users.User", related_name="cart", on_delete=models.CASCADE)
    coupon = models.ForeignKey(
        verbose_name=_("Coupon"),
        to="orders.Coupon",
        related_name="carts",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # items
    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return f"{self.user.username}'s Cart"


class CartOrderItem(BaseModel):
    cart = models.ForeignKey(verbose_name=_('Cart'), to='orders.Cart', related_name='items', on_delete=models.CASCADE)
    order = models.ForeignKey(verbose_name=_('Order'), to='orders.Order', related_name='items', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(
        verbose_name=_("Product name"),
        to="store.Product",
        related_name="entries",
        on_delete=models.SET_NULL,
        null=True
    )
    delivery_service = models.ForeignKey(
        verbose_name=_("Delivery service"),
        to="services.DeliveryService",
        related_name="entries",
        on_delete=models.SET_NULL,
        null=True
    )
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"), default=0)

    class Meta:
        verbose_name = _('Cart/Order item')
        verbose_name_plural = _('Cart/Order items')
        unique_together = ['cart', 'product']

    @property
    def price(self):
        if self.product.price_per_unit:
            return self.quantity * self.product.price_per_unit
        elif self.product.price_ranges.exists():
            ranges = self.product.price_ranges.all().order_by('quantity_from')
            price = None
            for r in ranges:
                if r.quantity_from <= self.quantity <= r.quantity_to:
                    price = r.price_per_unit
            if not price:
                raise ValueError(f'There is something wrong this the price of product {self.product.title, self.product.id}')
            return price
        else:
            raise ValueError(f'The product {self.product.title, self.id} doesn\'t have a price yet!')

    def __str__(self):
        return f"Cart entry {self.id} with {self.product.title}"


class Coupon(BaseModel):
    users = models.ManyToManyField(verbose_name=_("Users who used the coupon"), to="users.User", related_name="coupons", blank=True)
    coupon_code = models.CharField(verbose_name=_("Coupon code"), max_length=24)
    discount = models.PositiveIntegerField(
        verbose_name=_("Coupon discount"),
        default=0,
        validators=[MaxValueValidator(100)]
    )
    expiry_date = models.DateTimeField(verbose_name=_("Expiry date"), default=timezone.now)
    times_can_be_used = models.PositiveIntegerField(verbose_name=_("Times can be used"), default=1)
    times_used = models.PositiveIntegerField(verbose_name=_("Times used"), default=0)
    is_active = models.BooleanField(verbose_name=_("Is active?"), default=True)

    class Meta:
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")

    def __str__(self):
        return f"Coupon {self.coupon_code}"
