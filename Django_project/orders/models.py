from shop.model_choices import DiscountTypes # noqa
from shop.mixins.models_mixins import PKMixin # noqa
from shop.constans import MAX_DIGITS, DECIMAL_PLACES # noqa
from django.db import models
from django.contrib.auth import get_user_model

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
        return f'{self.amount} | {self.is_active}'


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

    def __str__(self):
        return f'{self.product.name} | {self.total_amount}'
