from .cart import Cart
from order.models import Order

def cart(request):
    return {'cart': Cart(request)}

def open_order(request):
    if request.user.is_authenticated:
        try:
            open_order = Order.objects.get(customer=request.user.customer, is_active=True)
        except:
            open_order = None
        return {'open_order': open_order.id}
    return {'open_order': None}
