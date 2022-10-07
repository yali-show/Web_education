from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html_join
from items.models import Item, Product, Category
from shop.mixins.image_mixins import ImageChange


@admin.register(Item)
class ItemAdmin(ImageChange, admin.ModelAdmin):
    list_display = ('name', 'created_at')

    # @admin.display(description='Image')
    # def show_image(self, instance):
    #     format_html_join(
    #         mark_safe('<br>'),
    #         '{}',
    #         ((line,) for line in instance.get_full_address()),
    #     ) or\
    #     mark_safe("<span class='errors'>I can't"
    #               " determine this address.</span>")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(Category)
class CategoryAdmin(ImageChange, admin.ModelAdmin):
    ...


