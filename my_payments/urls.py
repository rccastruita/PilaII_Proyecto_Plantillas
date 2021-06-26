from django.urls import path
from .views import PurchaseConfirmPage, PurchasePaymentPage, payment_details, start_purchase

urlpatterns = [
    path('checkout/', PurchaseConfirmPage.as_view(), name='checkout'),
    path('payment_details/<int:payment_id>', payment_details, name='payment_details'),
    path('start_purchase/', start_purchase, name='start_purchase'),
]