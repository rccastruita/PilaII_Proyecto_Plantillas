from django import forms
from payments import get_payment_model

class PaymentClientForm(forms.ModelForm):
    class Meta:
        model = get_payment_model()
        fields = [
            'billing_first_name',
            'billing_last_name',
            'billing_address_1',
            'billing_address_2',
            'billing_city',
            'billing_postcode',
            'billing_country_code',
            'billing_country_area',
            'customer_ip_address',
        ]