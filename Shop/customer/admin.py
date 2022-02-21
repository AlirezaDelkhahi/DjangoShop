from django.contrib import admin
from .models import Customer, Address

from core.models import User


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user']
    fields = ['user', 'gender', 'image']
    list_filter = ('last_updated', )
