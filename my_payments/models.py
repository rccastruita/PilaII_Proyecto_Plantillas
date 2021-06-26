from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy

from payments import PurchasedItem
from payments.models import BasePayment

class Purchase(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases', on_delete=models.PROTECT)

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='items', on_delete=models.PROTECT)

    name = models.CharField(max_length=80)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    sku = models.CharField(max_length=40)
    tax_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class Payment(BasePayment):
    purchase_info = models.OneToOneField(Purchase, on_delete=models.PROTECT, related_name='payment_info')

    def get_failure_url(self):
        return reverse('soon')

    def get_success_url(self):
        return reverse('cart')

    def get_purchased_items(self):
        yield None