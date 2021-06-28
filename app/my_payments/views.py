from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.conf import settings

from payments import get_payment_model, RedirectNeeded
from .models import Purchase, PurchaseItem
from shopping.models import ProductPresentation
from .forms import PaymentClientForm

def payment_details(request, payment_id):    
    payment = get_object_or_404(get_payment_model(), id=payment_id)
    if request.method == 'POST':
        client_form = PaymentClientForm(request.POST, instance=payment)
        if client_form.is_valid():
            payment = client_form.save()
            try:
                form = payment.get_form(data=request.POST or None)
            except RedirectNeeded as redirect_to:
                return redirect(str(redirect_to))
            return TemplateResponse(request, 'my_payments/payment.html',
                                    {'form': form, 'payment': payment})

def purchase_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)
    
    if request.method == 'GET':
        client_form = PaymentClientForm(instance=payment)
        return TemplateResponse(request, 'my_payments/client_form.html',
            {'form': client_form, 'payment': payment})

class PurchaseConfirmPage(TemplateView):
    template_name = 'my_payments/confirm.html'

def start_purchase(request):
    if request.method == 'POST':
        purchase = Purchase.objects.create(
            user = request.user,
        )
        purchase.save()

        for item in request.user.cart.all():
            purchase_item = PurchaseItem.objects.create(
                purchase = purchase,
                name = str(item),
                quantity = item.count,
                price = item.get_amount(),
                currency = settings.CURRENCY,
                sku = str(item.presentation.pk),
                tax_rate = settings.TAX,
            )
            purchase_item.save()

        Payment = get_payment_model()
        payment = Payment.objects.create(
            purchase_info = purchase,
            variant = 'default',
            description = 'Compra en Laura\'s Bakery',
            total = request.user.get_cart_subtotal(),
            tax = settings.TAX,
            currency = settings.CURRENCY,
            delivery = settings.DELIVERY_FEE,
            billing_first_name = '',
            billing_last_name = '',
            billing_address_1 = '',
            billing_address_2 = '',
            billing_city = '',
            billing_postcode = '',
            billing_country_code = '',
            billing_country_area = '',
            customer_ip_address = '127.0.0.1',
        )
        payment.save()

        return redirect('purchase_details', payment_id=payment.pk)

    else:
        return redirect('checkout')

def payment_accepted(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)
    purchase = payment.purchase_info

    if not purchase.delivered:
        for purchase_item in purchase.items.all():
            product = ProductPresentation.objects.get(pk=int(purchase_item.sku))
            product.inventory -= purchase_item.quantity
            product.save()

        request.user.cart.all().delete()
        purchase.delivered = True
        purchase.save()

    return redirect('home')