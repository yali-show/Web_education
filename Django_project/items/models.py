from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    price = models.PositiveIntegerField()
    sku = models.CharField(max_length=255)


class Discount(models.Model):
    amount = models.PositiveIntegerField()
    code = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    discount_type = models.IntegerField(choices=((0, 'money'), (1,'percents')))
