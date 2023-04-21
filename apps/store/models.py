from autoslug import AutoSlugField
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from . import choices


class Category(BaseModel):
    title = models.CharField(verbose_name=_('Category title'), max_length=124)
    slug = AutoSlugField(verbose_name=_('Category slug'), populate_from='title', max_length=124)

    # subcategories

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Subcategory(BaseModel):
    parent_category = models.ForeignKey(
        verbose_name=_('Parent category'),
        to='store.Category',
        related_name='subcategories',
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(verbose_name=_('Subcategory title'), max_length=124)
    slug = AutoSlugField(verbose_name=_('Subcategory slug'), populate_from='title', max_length=124, unique=True)
    photo = models.ImageField(verbose_name=_('Subcategory photo'), upload_to='images/store/subcategory_photos/')

    # products

    class Meta:
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')

    def __str__(self):
        return f"Subcategory {self.title}"


class Product(BaseModel):
    category = models.ForeignKey(
        verbose_name=_('Category'),
        to='store.Subcategory',
        related_name='products',
        on_delete=models.SET_NULL,
        null=True
    )
    brand = models.ForeignKey(
        verbose_name=_('Brand'),
        to='store.Brand',
        related_name='products',
        on_delete=models.SET_NULL,
        null=True
    )
    supplier = models.ForeignKey(
        verbose_name=_('Supplier'),
        to='services.Supplier',
        related_name='products',
        on_delete=models.SET_NULL,
        null=True
    )
    buyers = models.ManyToManyField(
        verbose_name=_('Buyers'),
        to='users.User',
        through='users.Rating',
        related_name='bought_products',
        blank=True
    )
    discount = models.PositiveIntegerField(
        verbose_name=_("Product discount"),
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    title = models.CharField(verbose_name=_('Product title'), max_length=255)
    initial_quantity = models.DecimalField(verbose_name=_('Initial quantity'), max_digits=24, decimal_places=2, default=0)
    sold_quantity = models.DecimalField(verbose_name=_('Sold quantity'), max_digits=24, decimal_places=2, default=0)
    price_per_unit = models.DecimalField(verbose_name=_('Price per unit'), max_digits=24, decimal_places=2, blank=True, null=True)

    condition = models.CharField(verbose_name=_('Condition'), choices=choices.PRODUCT_CONDITION, max_length=3, default='bra')
    description = models.TextField(verbose_name=_('Product description'))

    # photos
    # price_ranges

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    @property
    def get_ranges(self):
        ranges = self.price_ranges.all()
        if ranges:
            response = dict()
            for x in range(0, len(ranges)):
                response[x] = {'from': ranges[x].quantity_from, 'to': ranges[x].quantity_to, 'price_per_unit': ranges[x].price_per_unit}
            return response
        else:
            return {'missing': 'No price ranges'}

    def clean_fields(self, exclude=None):
        if self.price_per_unit and self.price_ranges.exists():
            raise ValidationError({'price_per_unit': 'You cannot have both price_per_unit and price_ranges assigned to an object at the same time!'})
        super().clean_fields()

    def __str__(self):
        return f"Product {self.title}"


class PriceRange(BaseModel):
    product = models.ForeignKey(verbose_name=_('Related parent product'), to='store.Product', related_name='price_ranges', on_delete=models.CASCADE)
    quantity_from = models.DecimalField(verbose_name=_('Beginning from'), max_digits=24, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    quantity_to = models.DecimalField(verbose_name=_('To and including'), max_digits=24, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    price_per_unit = models.DecimalField(verbose_name=_('Price per unit'), max_digits=24, decimal_places=2, default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = _('Price range')
        verbose_name_plural = _('Price ranges')
        ordering = ['quantity_from']

    def clean_fields(self, exclude=None):
        if self.quantity_from >= self.quantity_to:
            raise ValidationError({"quantity_from": "Quantity 'Beginning from' should be smaller than quantity 'To and including'!"})
        super().clean_fields()

    def __str__(self):
        return f"Price range from {self.quantity_from} to {self.quantity_to}"


class ProductPhoto(BaseModel):
    product = models.ForeignKey(verbose_name=_('Related parent product'), to='store.Product', related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name=_('Product photo'), upload_to='images/store/products/%Y/%m/%d')

    class Meta:
        verbose_name = _('Product photo')
        verbose_name_plural = _('Product photos')


class Brand(BaseModel):
    title = models.CharField(verbose_name=_('Brand name'), max_length=255)
    logo = models.ImageField(verbose_name=_('Brand logo'), upload_to='images/store/brand_logos/')

    # products

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return f"Brand - {self.title}"


class DealAndOffer(BaseModel):
    pass
