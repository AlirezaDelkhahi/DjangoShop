from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel
import os


class Address(BaseModel):
    """
        Customer's Addresses (a customer can have multiple addresses)
    """
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    address = models.TextField()
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, related_name='userAddress')

    def __str__(self):
        return f'{self.customer} {self.city}'


def get_upload_path(instance, filename):
    return os.path.join(
        instance.id,
        instance.first_name, instance.last_name,
        filename
        )    


class Customer(BaseModel):
    
    gender_choices = (
        ('male', 'مذکر'),
        ('female', 'مونث')
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    phone = models.CharField(max_length=100, verbose_name='Phone Number')
    image = models.FileField(default='Default-Images/default_user,png', upload_to='user_profiles/', blank=True, null=True, verbose_name='Profile Image')
    gender = models.CharField(choices=gender_choices, null=True, blank=True, verbose_name='Gender', max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
