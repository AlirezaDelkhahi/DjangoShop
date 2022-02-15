from django.db import models
from core.models import BaseDiscount, BaseModel
from product.models import Product
# Create your models here.


class Coupon(BaseDiscount):
    code = models.CharField(max_length=50)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    def __str__(self):
        if self.type == 'percent':
            return f'{self.code}| {self.value}%'
        return f'{self.code}| {self.value}$'


class CartItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Item')
    quantity = models.IntegerField(default=1, verbose_name='Quantity')

    def __str__(self):
        return f'{self.product.name}: {self.quantity}x'
