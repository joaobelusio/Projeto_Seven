from django.db import models
from orders.models import Order

class Coupon(models.Model):
    code = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    discount_type = models.CharField(max_length=50)  # Pode ser 'percentual' ou 'fixo'
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    usage_limit = models.IntegerField(null=True, blank=True)
    used_count = models.IntegerField(default=0)
    min_purchase_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.code

class OrderCoupon(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='applied_coupons')
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, related_name='orders')
    applied_discount_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Coupon {self.coupon.code} applied to Order {self.order.id}"
