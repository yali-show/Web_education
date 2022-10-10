from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html_join
from items.models import Item, Product, Category
from shop.mixins.image_mixins import ImageChange


@admin.register(Item)
class ItemAdmin(ImageChange, admin.ModelAdmin):
    list_display = ('name', 'created_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(Category)
class CategoryAdmin(ImageChange, admin.ModelAdmin):
    ...


