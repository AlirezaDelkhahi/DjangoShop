from django.urls import path
from .views import index, DetailCategory, DetailProduct
app_name = 'product'

urlpatterns = [
    path('', index, name='home'),
    path('products/<int:product_id>', DetailProduct.as_view(), name='product-detail'),
    path('categories/<int:category_id>', DetailCategory.as_view(), name='category-detail')
]