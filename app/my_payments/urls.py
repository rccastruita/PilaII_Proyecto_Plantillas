from django.urls import path
from .views import PurchaseConfirmPage, payment_details, start_purchase, payment_accepted, purchase_details

urlpatterns = [
    path('checkout/', PurchaseConfirmPage.as_view(), name='checkout'),
    path('payment_details/<int:payment_id>', payment_details, name='payment_details'),
    path('start_purchase/', start_purchase, name='start_purchase'),
    path('payment_accepted/<int:payment_id>', payment_accepted, name='payment_accepted'),
    path('purchase_details/<int:payment_id>', purchase_details, name='purchase_details'),
]