from django.db import models
from orders.models import Order

class Shipment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipment')
    tracking_number = models.CharField(max_length=255, blank=True, null=True)
    delivery_status = models.CharField(max_length=255, default='awaiting dispatch')
    shipping_method = models.CharField(max_length=255)
    shipped_date = models.DateTimeField()
    estimated_delivery_date = models.DateTimeField()
    delivery_address = models.TextField()

    def __str__(self):
        return f"Shipment for Order {self.order.id} - Tracking Number: {self.tracking_number}"
