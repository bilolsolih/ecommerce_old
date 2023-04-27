from django.db import models


class ShippingTypes(models.TextChoices):
    WWS = ('wws', 'Worldwide shipping')
    CWS = ('cws', 'Countrywide shipping')
    LCL = ('lcl', 'Local shipping')
