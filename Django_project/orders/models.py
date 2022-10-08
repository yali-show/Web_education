from shop.model_choices import DiscountTypes
from shop.mixins.models_mixins import PKMixin
from shop.constans import MAX_DIGITS, DECIMAL_PLACES
from django.db import models
from django.contrib.auth import get_user_model
from decimal import Decimal

User = get_user_model()


class Discount(PKMixin):
    amount = models.PositiveIntegerField(default=0)
    code = models.CharField(max_length=32),
    is_active = models.BooleanField(default=True),
    discount_type = models.PositiveSmallIntegerField(
        choices=DiscountTypes.choices,
        default=DiscountTypes.Value

    )

    def __str__(self):
        return f'{self.amount} | {bool(self.is_active)}'


class Order(PKMixin):
    total_amount = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=0
    )
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)

    product = models.ManyToManyField('items.Product')
    discount = models.ForeignKey(Discount,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)

    def with_discount(self):
        if self.discount:
            if self.discount.discount_type == DiscountTypes.Value:
                return self.total_amount - self.discount.amount
            elif self.discount.discount_type == DiscountTypes.PERCENT:
                return (self.total_amount - (self.total_amount / 100 * self.discount.amount)).quantize(Decimal('.01'))

    def __str__(self):
        return f'{self.product.name} | {self.total_amount}'
