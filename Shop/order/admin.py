from django.contrib import admin
from .models import Coupon, Cart, CartItem
# Register your models here.


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'value', 'type', 'max_price', 'valid_from', 'valid_to', 'is_active']
    search_fields = ('code',)
    list_filter = ['last_updated']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['customer', 'discount', 'address']
    search_fields = ('customer', 'address')
    list_filter = ['last_updated']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']
    search_fields = ('product', )
    list_filter = ['last_updated']
