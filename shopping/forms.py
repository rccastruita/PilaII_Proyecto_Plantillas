from django import forms

from .models import CartItem

# Form for posting and editing comments
class CartItemModelForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['presentation', 'count']
        labels = {
            'presentation': 'Presentación',
            'count': 'Cantidad',
        }