from django.db import models
from core.models import BaseDiscount, BaseModel
from customer.models import Customer
from product.models import Product


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
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')

    @property
    def final_price(self):
        """
         Calculate and Return the Final Price of an order item
        :param: instance
        :return: final_price
        """
        if self.product.discount:
            return self.product.price - self.product.discount.profit_value(self.product.price) * self.quantity
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.product.name}: {self.quantity}x'

