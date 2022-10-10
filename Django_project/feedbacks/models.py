from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from shop.mixins.models_mixins import PKMixin

User = get_user_model()


class Feedback(PKMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField(validators=(MaxValueValidator(5),))
