from django.db import models
from core.models import BaseModel
from customer.models import Address
from core.models import BaseDiscount


class Category(BaseModel):
    """
        Category Model has Self Relation
    """
    name = models.CharField(max_length=100)
    thumbnail = models.FileField(default='Default-Images/default_category.png')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='children', null=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.name}'


class Provider(BaseModel):
    """
        Provider Companies Bring Product lines of different brands
    """
    name = models.CharField(max_length=100, verbose_name='Company Name')
    description = models.TextField(max_length=100, verbose_name='Company Details', null=True, blank=True)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.name}'


class Brand(BaseModel):
    """
        Product's original brands
    """
    name = models.CharField(max_length=100, verbose_name='Brand Name')
    country = models.CharField(max_length=100, verbose_name='Brand Country')
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, verbose_name='Brand Provider',
                                 null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name='Brand Details')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.name} from {self.provider}'


class Discount(BaseDiscount):
    """
        Discount model for Products
    """
    expire_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        if self.type == 'percent':
            return f'{self.value}%'
        return f'{self.value}$'


class Product(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    slug = models.SlugField(null=True)
    price = models.IntegerField(verbose_name='Price')
    category = models.ForeignKey(Category, verbose_name='Category',
                                 related_name='products', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    image = models.FileField(default='Default-Images/product_default.jpg', upload_to='Products/', null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Brand',
                              related_name='products')
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Discount', related_name='products', default=None)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.name} {self.price}'