from django.db import models
from django.conf import settings

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=50, default='pending')
    payment_status = models.CharField(max_length=50, default='pending')
    payment_details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"

class OrderCoupon(models.Model):
    order = models.ForeignKey(Order, related_name='coupons', on_delete=models.CASCADE)
    coupon = models.ForeignKey('marketing.Coupon', on_delete=models.CASCADE)
    applied_discount_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Coupon {self.coupon.code} for Order {self.order.id}"

class AffiliateSale(models.Model):
    order = models.ForeignKey(Order, related_name='affiliate_sales', on_delete=models.CASCADE)
    affiliate_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    commission = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Affiliate Sale {self.id} - Order {self.order.id}"
