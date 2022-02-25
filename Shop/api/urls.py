# Shop Url configs
from django.urls import path, include
from .views import UserListView, AddressDetailView, AddressListView, UserDetailView

app_name = 'api'

urlpatterns = [
    path('user-list', UserListView.as_view(), name='user-list'),
    path('address-list', AddressListView.as_view(), name='address-list'),
    path('user-detail/<pk>', UserDetailView.as_view(), name='user-detail'),
    path('address-detail/<pk>', AddressDetailView.as_view(), name='address-detail'),
]