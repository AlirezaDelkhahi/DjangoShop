from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    """
        Customer's Addresses (a customer can have multiple addresses)
    """
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    address = models.TextField()
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, related_name='userAddress')