from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import Category, Product, Brand
# Create your views here.


def index(request):
    """
        This view just returns last 10 products in a home template
    """
    cats = Category.objects.filter(parent__isnull=True).exclude(children__isnull=True)
    products = Product.objects.all()[:10]
    return render(request, 'product/index.html', {'cats': cats, 'products': products})


class DetailCategory(View):
    """
        This view returns a requested category to show products of it
    """
    template_name = 'product/detail-category.html'

    def dispatch(self, request, *args, **kwargs):
        """
            checks if category has product or not
        """
        category: Category = Category.objects.get(id=kwargs['category_id'])
        if not category.products.all():  # category products is empty
            return redirect('product:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, category_id):
        """
            returns requested category
            :params: category_id
            :return: category
        """
        cat = Category.objects.get(id=category_id)
        return render(request, self.template_name, {'cat':cat})


class DetailProduct(View):
    """
        this view returns more details about a requested product
    """
    template_name = 'product/detail-product.html'

    def setup(self, request, *args, **kwargs):
        self.product = get_object_or_404(Product, pk=kwargs['product_id'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, product_id):
        print(self.product.brand)
        return render(request, self.template_name, {'product': self.product})

    def post(self, requset, product_id):
        pass


class ListBrand(View):
    """
        This View shows all existing brands with a button to show products of them
    """
    template_name = 'product/brands.html'

    def get(self, request):
        return render(request, self.template_name, {'brands': Brand.objects.all()})


class DetailBrand(View):
    """
        This view shows all existing products for a requested brand
    """
    template_name = 'product/detail-brand.html'

    def dispatch(self, request, *args, **kwargs):
        """
            checks if brand has product or not
        """
        brand: Brand = Brand.objects.get(id=kwargs['brand_id'])
        if not brand.products.all():  # category products is empty
            return redirect('product:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, brand_id):
        """
            returns requested brand
            :params: brand_id
            :return: brand
        """
        brand = Brand.objects.get(id=brand_id)
        return render(request, self.template_name, {'brand': brand})