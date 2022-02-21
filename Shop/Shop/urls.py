# Shop Url configs
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path(''),
    path('customer', include('customer.urls', namespace='customer')),
    path('product', include('product.urls', namespace='product')),
    path('order', include('order.urls', namespace='order')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)