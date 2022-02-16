from django.contrib import admin
from .models import Product, Category, Discount, Brand, Provider
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ('name', 'slug', 'category', 'price')
    list_filter = ['last_updated']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',)
    list_filter = ['last_updated']


@admin.register(Discount)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['value', 'type', 'is_active']
    search_fields = ('value', 'type',)
    list_filter = ['last_updated']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'provider']
    search_fields = ('name', 'provider', 'country')
    list_filter = ['last_updated']


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name', )
    list_filter = ['last_updated']