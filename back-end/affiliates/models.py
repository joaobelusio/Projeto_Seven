from django.db import models
from django.conf import settings
from orders.models import Order

class Affiliate(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='affiliate_profile')
    total_commission_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_sales_generated = models.IntegerField(default=0)

    def __str__(self):
        return f"Affiliate {self.user.email}"

class AffiliateSale(models.Model):
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE, related_name='sales')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='affiliate_sales')
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sale_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale {self.order.id} - Affiliate {self.affiliate.user.email} - Commission {self.commission_amount}"
