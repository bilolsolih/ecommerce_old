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
    postal_code = models.CharField(verbose_name=_('Postal code'), max_length=20)
    country = models.CharField(verbose_name=_('Country'), max_length=100)
    region = models.CharField(verbose_name=_('Region'), max_length=100)
    city = models.CharField(verbose_name=_('City'), max_length=100)
    street = models.CharField(verbose_name=_('Street'), max_length=100)

    coupon = models.ForeignKey(verbose_name=_('Coupon'), to='orders.Coupon', related_name='orders', on_delete=models.SET_NULL, null=True)
    price_before_discount = models.DecimalField(verbose_name=_('Price before discount'), max_digits=24, decimal_places=2, default=0)
    price_after_discount = models.DecimalField(verbose_name=_('Price after discount'), max_digits=24, decimal_places=2, default=0)

    paid = models.BooleanField(verbose_name=_('Paid'), default=False)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class OrderItem(BaseModel):
    order = models.ForeignKey(verbose_name=_('Parent order'), to='orders.Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(verbose_name=_('Product'), to='store.Product', related_name='order_items', on_delete=models.CASCADE)
    delivery_service = models.ForeignKey(
        verbose_name=_("Delivery service"),
        to="services.DeliveryService",
        related_name="order_items",
        on_delete=models.SET_NULL,
        null=True,
    )
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

    # items
    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return f"{self.user.username}'s Cart"


class CartItem(BaseModel):
    the_cart = models.ForeignKey(verbose_name=_('Cart'), to='orders.Cart', related_name='items', on_delete=models.CASCADE)
    the_product = models.ForeignKey(
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
        verbose_name = _('Cart item')
        verbose_name_plural = _('Cart items')
        unique_together = ['the_cart', 'the_product']

    @property
    def price(self):
        if self.the_product.price_per_unit:
            return self.quantity * self.the_product.price_per_unit
        elif self.the_product.price_ranges.exists():
            ranges = self.the_product.price_ranges.all().order_by('quantity_from')
            price = None
            for r in ranges:
                if r.quantity_from <= self.quantity <= r.quantity_to:
                    price = r.price_per_unit
            if not price:
                raise ValueError(f'There is something wrong this the price of the_product {self.the_product.title, self.the_product.id}')
            return price
        else:
            raise ValueError(f'The product {self.the_product.title, self.id} doesn\'t have a price yet!')

    def __str__(self):
        return f"Cart entry {self.id} with {self.the_product.title}"


