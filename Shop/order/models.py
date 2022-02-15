from django.db import models
from core.models import BaseDiscount
# Create your models here.


class Coupon(BaseDiscount):
    code = models.CharField(max_length=50)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    def __str__(self):
        if self.type == 'percent':
            return f'{self.code}| {self.value}%'
        return f'{self.code}| {self.value}$'
