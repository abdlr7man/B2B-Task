from django.shortcuts import render
from Orders import models as Orders_models

def home_page(request):
    orders = Orders_models.Order.objects.all()
    return render(request, "home.html", {"orders": orders })


def order_details_page(request, order_id):
    order = Orders_models.Order.objects.get(id=order_id)
    order_payments_confirmations = Orders_models.OrderPaymentConfirmation.objects.filter(related_order=order)
    return render(request, 'order_confirmation_details.html', {'order_payments_confirmations':order_payments_confirmations})