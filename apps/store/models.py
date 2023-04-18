from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

from . import choices

"""
Category - List, Retrieve
Subcategory - List, Retrieve
Item - List, Retrieve
Brand - List, Retrieve

"""


class Category(BaseModel):
    title = models.CharField(verbose_name=_("Category title"), max_length=124)
    slug = AutoSlugField(verbose_name=_("Category slug"), populate_from="title", max_length=124)

    # subcategories

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Subcategory(BaseModel):
    parent_category = models.ForeignKey(
        verbose_name=_("Parent category"),
        to="store.Category",
        related_name="subcategories",
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(verbose_name=_("Subcategory title"), max_length=124)
    slug = AutoSlugField(verbose_name=_("Subcategory slug"), populate_from="title", max_length=124, unique=True)
    photo = models.ImageField(verbose_name=_("Subcategory photo"), upload_to="images/store/subcategory_photos/")

    # items

    class Meta:
        verbose_name = _("Subcategory")
        verbose_name_plural = _("Subcategories")

    def __str__(self):
        return self.title


class Item(BaseModel):
    category = models.ForeignKey(
        verbose_name=_("Category"), to="store.Subcategory", related_name="items", on_delete=models.SET_NULL, null=True
    )
    brand = models.ForeignKey(
        verbose_name=_("Brand"), to="store.Brand", related_name="items", on_delete=models.SET_NULL, null=True
    )
    title = models.CharField(verbose_name=_("Item title"), max_length=255)
    photo = models.ImageField(verbose_name=_("Item photo"), upload_to="images/store/items/%Y/%m/%d")
    # TODO bir nechta rasm yuklasa bo'ladigan qilish kerak

    initial_quantity = models.DecimalField(
        verbose_name=_("Initial quantity"), max_digits=24, decimal_places=2, default=0
    )
    sold_quantity = models.DecimalField(verbose_name=_("Sold quantity"), max_digits=24, decimal_places=2, default=0)
    price_per_unit = models.DecimalField(verbose_name=_("Price per unit"), max_digits=24, decimal_places=2, default=0)
    # 10-20 90$, 21-30 85$
    # TODO PriceRange degan model qilish kerak
    condition = models.CharField(
        verbose_name=_("Condition"), choices=choices.ITEM_CONDITION, max_length=3, default="bra"
    )
    description = models.TextField(verbose_name=_("Item description"))

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return f"Item {self.title}"


class Brand(BaseModel):
    title = models.CharField(verbose_name=_("Brand name"), max_length=255)
    logo = models.ImageField(verbose_name=_("Brand logo"), upload_to="images/store/brand_logos/")

    # items

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return f"Brand - {self.title}"


class DealAndOffer(BaseModel):
    pass
