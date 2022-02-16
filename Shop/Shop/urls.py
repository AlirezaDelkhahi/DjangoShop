# Shop Url configs
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from product.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

