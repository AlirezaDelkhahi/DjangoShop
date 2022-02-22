from django.urls import path
from .views import index, DetailCategory, DetailProduct, ListBrand, DetailBrand
app_name = 'product'

urlpatterns = [
    path('', index, name='home'),
    path('products/<int:product_id>', DetailProduct.as_view(), name='product-detail'),
    path('categories/<int:category_id>', DetailCategory.as_view(), name='category-detail'),
    path('brands/', ListBrand.as_view(), name='brand-list'),
    path('brands/<int:brand_id>', DetailBrand.as_view(), name='brand-detail'),
]