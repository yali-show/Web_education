from django.contrib import admin
from orders.models import Order, Discount


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['total_amount', 'total_amount_with_discount']

    def total_amount_with_discount(self, obj):
        return obj.with_discount()


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    ...

