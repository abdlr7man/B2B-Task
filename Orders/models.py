from django.db import models

# Create your models here.

class Order(models.Model):
    order_id = models.CharField(max_length=100, verbose_name="Order ID")
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__ (self):
        return f"{self.order_id}"

class OrderPaymentConfirmation(models.Model):
    order_confirmation_status = models.CharField(max_length=100, verbose_name="Order Confirmation Status")
    related_order = models.ForeignKey(Order, verbose_name=("Related order"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Order Payment Confirmation"
        verbose_name_plural = "Order Payment Confirmations"

    def __str__ (self):
        return f"{self.order_confirmation_status}"