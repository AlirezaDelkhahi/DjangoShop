from django.urls import path
from .views import index, DetailCategory
app_name = 'product'

urlpatterns = [
    path('', index, name='home'),
    path('categories/<int:category_id>', DetailCategory.as_view(), name='category-detail')
]