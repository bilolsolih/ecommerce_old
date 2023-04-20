from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Order(BaseModel):
    user = models.ForeignKey(
        verbose_name=_('User who made this order'),
        to='users.User',
        related_name='orders',
        on_delete=models.SET_NULL,
        null=True
    )
    address = models.CharField(verbose_name=_('Address'), max_length=250)
    postal_code = models.CharField(verbose_name=_('Postal code'), max_length=20)
    city = models.CharField(verbose_name=_('City'), max_length=100)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class OrderItem(models.Model):
    order = models.ForeignKey(verbose_name=_('Parent order'), to='orders.Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(verbose_name=_('Product'), to='store.Product', related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'), default=1)

    class Meta:
        verbose_name = _('Order item')
        verbose_name_plural = _('Order items')

    def __str__(self):
        return str(self.id)


class Cart(BaseModel):
    user = models.OneToOneField(verbose_name=_("Customer"), to="users.User", related_name="cart", on_delete=models.CASCADE)
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
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return f"{self.user.username}'s Cart"


class CartEntry(BaseModel):
    cart = models.ForeignKey(verbose_name=_("Parent cart"), to="orders.Cart", related_name="entries", on_delete=models.CASCADE)
    product = models.ForeignKey(
        verbose_name=_("Product name"),
        to="store.Product",
        related_name="entries",
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
        verbose_name = _("Cart entry")
        verbose_name_plural = _("Cart entries")
        unique_together = ['cart', 'product']

    def __str__(self):
        return f"Cart entry {self.id} with {self.product.title}"


class Coupon(BaseModel):
    users = models.ManyToManyField(verbose_name=_("Users who used the coupon"), to="users.User", related_name="coupons", blank=True)
    coupon_code = models.CharField(verbose_name=_("Coupon code"), max_length=24)
    discount = models.PositiveIntegerField(
        verbose_name=_("Coupon discount"),
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
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
