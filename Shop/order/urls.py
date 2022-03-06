from django.urls import path
from .views import CartView
app_name = 'order'

urlpatterns = [
    path('add_to_cart/<int:product_id>/<int:quantity>', CartView.as_view(), name='cart')
]