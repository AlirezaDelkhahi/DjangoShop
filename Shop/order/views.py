from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views import View
from .cart import Cart
from product.models import Product
from django.shortcuts import get_object_or_404
from order.forms import AddressForm
# Create your views here.


class CartView(View):

    def setup(self, request, *args, **kwargs):
        self.cart = Cart(request)
        return super().setup(request, *args, **kwargs)  

    def post(self,request, product_id, quantity):
        product = get_object_or_404(Product, pk=product_id)
        self.cart.add(product, quantity)
        return JsonResponse({'TotalItems': self.cart.__len__(), 'url':reverse('order:cart-list')}, safe=False)
    
    

class CartList(View):
    template_name = 'order/cart.html'

    def get(self, request):
        return render(request, self.template_name)

class CartDetails(View):
    template_name = 'order/cart_detail.html'

    def get(self, request):
        return render(request, self.template_name, { 'address_form':AddressForm(customer=request.user.customer)})  

class CartItemDelete(View):

    def setup(self, request, *args, **kwargs):
        self.cart = Cart(request)
        return super().setup(request, *args, **kwargs)

    def delete(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        self.cart.remove(product=product)
        return JsonResponse({'TotalItems': self.cart.__len__(), 'url':reverse('order:cart-list'), 'total_price':self.cart.get_total_price()}, safe=False)


