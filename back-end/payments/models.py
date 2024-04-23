from django.db import models

class Payment(models.Model):
    order = models.OneToOneField('orders.Order', on_delete=models.CASCADE, related_name='payment')
    payment_status = models.CharField(max_length=50, default='pending')
    payment_details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment for Order {self.order.id}"
