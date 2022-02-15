from django.contrib import admin
from .models import Coupon
# Register your models here.


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    fields = ['code', 'value', 'type', 'max_price', 'valid_from', 'valid_to', 'is_active']