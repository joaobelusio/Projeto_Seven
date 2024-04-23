from django.contrib import admin
from .models import Coupon, OrderCoupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_type', 'discount_amount', 'discount_percent', 'is_active', 'valid_from', 'valid_until']
    list_filter = ['is_active', 'discount_type']
    search_fields = ['code', 'description']

@admin.register(OrderCoupon)
class OrderCouponAdmin(admin.ModelAdmin):
    list_display = ['order', 'coupon', 'applied_discount_amount']
    search_fields = ['order__id', 'coupon__code']
