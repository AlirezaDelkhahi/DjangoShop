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
