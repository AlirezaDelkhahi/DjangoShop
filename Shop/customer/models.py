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

class Customer(models.Model):
    
    gender_choices = (
        ('male','مذکر'),
        ('female','مونث')
        )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    phone = models.CharField(max_length=100, verbose_name='Phone Number')
    image = models.FileField(default='Default-Images/default_user,png', upload_to=img_path, blank=True, null=True, verbose_name='Profile Image')
    gender = models.CharField(choices=gender_choices, null=True, blank=True, verbose_name='Gender')

    @property
    def img_path(self):
        """
            this property creates a dynamic directory name for each user
        """
        return f'{self.id}-{self.first_name}_{self.last_name}'