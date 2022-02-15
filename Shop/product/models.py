from django.db import models
from core.models import BaseModel
from customer.models import Address


class Category(BaseModel):
    """
        Category Model has Self Relation
    """
    name = models.CharField(max_length=100)
    thumbnail = models.FileField(default='Default-Images/default_category.png')
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Provider(BaseModel):
    """
        Provider Companies Bring Product lines of different brands
    """
    name = models.CharField(max_length=100, verbose_name='Company Name')
    description = models.TextField(max_length=100, verbose_name='Company Details', null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
