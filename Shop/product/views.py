from django.shortcuts import render, redirect
from django.views import View

from .models import Category, Product
# Create your views here.


def index(request):
    cats = Category.objects.filter(parent__isnull=True).exclude(children__isnull=True)
    products = Product.objects.all()[:10]
    return render(request, 'product/index.html', {'cats': cats, 'products': products})


class DetailCategory(View):
    template_name = 'product/detail-category.html'

    def dispatch(self, request, *args, **kwargs):
        category: Category = Category.objects.get(id=kwargs['category_id'])
        if not category.products.all():
            return redirect('product:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, category_id):
        cat = Category.objects.get(id=category_id)
        return render(request, self.template_name, {'cat':cat})