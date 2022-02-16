from django.db import models
from django.utils import timezone
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


class Cart(BaseModel):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE,
                                    verbose_name='Customer', related_name='customer',
                                    null=True, blank=True)
    discount = models.IntegerField(verbose_name='Coupon', blank=True, null=True, default=0)
    address = models.TextField(verbose_name='Shipping Address', null=True, blank=True)

    @property
    def total_price(self):
        """
            Calculate and return total_price of Cart (without Coupon)
        """
        return sum([x.final_price for x in self.items.all()])

    @property
    def final_price(self):
        """
            Calculate and return final_price of Cart (with Coupon)
            :param: self
            :return: final_price
        """
        total_price = sum([x.final_price for x in self.items.all()])
        if self.discount:
            return total_price - self.discount
        return total_price

    def add_coupon(self, coupon: Coupon):
        """
            validates and calculates profit of a coupon and gives it to cart's discount field
            :param: coupon instance
            :return: profit discount (if coupon is  valid)
        """
        if coupon.is_active and (coupon.valid_from <= timezone.now() <= coupon.valid_to):
            self.discount = coupon.profit_value(self.final_price)
        return self.discount

    def __str__(self):
        return f'{self.customer} - {self.final_price}'
