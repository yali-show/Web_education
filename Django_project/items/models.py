import os
from django.db import models
from django.core.validators import MinValueValidator
from shop.mixins.models_mixins import PKMixin # noqa


def upload_to(instance, filename):
    _name, extencion = os.path.splitext(filename)
    return f'images/{instance.__class__.__name__.lower()}/' \
        f'{instance.pk}/image{extencion}'


class Category(PKMixin):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} | {self.description}'


class Item(PKMixin):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('items.Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category.name}'


class Product(PKMixin):
    name = models.CharField(max_length=255)
    price = models.PositiveSmallIntegerField(
        validators=[MinValueValidator]

    )
    sku = models.CharField(max_length=32, blank=True, null=True)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f'{self.items.name}: {self.price}'
