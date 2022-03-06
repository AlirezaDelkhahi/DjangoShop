from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .cart import Cart
from product.models import Product
from django.shortcuts import get_object_or_404
# Create your views here.


class CartView(View):
    template_name = 'order/cart.html'

    def setup(self, request, *args, **kwargs):
        self.cart = Cart(request)
        return super().setup(request, *args, **kwargs)

    # def get(self, request):
    #     return render(request, template_name, {"cart": self.cart})

    def post(self,request, product_id, quantity):
        product = get_object_or_404(Product, pk=product_id)
        self.cart.add(product, quantity)
        return HttpResponse('ok')