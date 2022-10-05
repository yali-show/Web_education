from django.db.models import IntegerChoices


class DiscountTypes(IntegerChoices):
    Value = 0
    PERCENT = 1
