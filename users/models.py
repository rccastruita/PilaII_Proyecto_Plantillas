from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from decimal import Decimal

class User(AbstractUser):
    """Custom User model"""
    email = models.EmailField(null=False, unique=True)
    city = models.ForeignKey("stores.City", null=True, blank=True, on_delete=models.SET_NULL)
    in_mailing_list = models.BooleanField(default=True)

    def get_cart_subtotal(self):
        subtotal = Decimal(0)
        for item in self.cart.all():
            subtotal += Decimal(item.count * item.presentation.price)
        return subtotal

    def get_cart_taxes(self):
        return self.get_cart_subtotal() * settings.TAX

    def get_cart_total(self):
        return Decimal(self.get_cart_subtotal() + self.get_cart_taxes())