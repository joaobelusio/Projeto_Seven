from django.contrib import admin
from .models import Affiliate, AffiliateSale

@admin.register(Affiliate)
class AffiliateAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_commission_earned', 'total_sales_generated']
    search_fields = ['user__email']

@admin.register(AffiliateSale)
class AffiliateSaleAdmin(admin.ModelAdmin):
    list_display = ['affiliate', 'order', 'commission_amount', 'sale_amount', 'created_at']
    search_fields = ['affiliate__user__email', 'order__id']
