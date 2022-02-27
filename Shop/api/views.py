from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication
from .serializers import UserSerializer, AddressSerializer, CustomerSerializer
from customer.models import Address, Customer
from core.models import User
from .APIpermissions import IsOwnerPermission, IsSuperUserPermission
import django_filters.rest_framework
from rest_framework import filters

# -------User Detail/List------------------

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserPermission]

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerPermission]

# -------Addresss Detail/List------------------

class AddressListView(generics.ListAPIView):
    serializer_class = AddressSerializer
    permission_classes = [IsOwnerPermission]

    def get_queryset(self):
        print(self.request.user)
        return Address.objects.filter(customer__user = self.request.user)

class AddressDetailView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsOwnerPermission]

# -------Customer Detail/List------------------

class CustomerDetailView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]    
    search_fields = ['id', 'user__phone', 'user__email']


# -------CartItem Detail/List------------------
#TODO: CartItem API VIEWS
# -------Cart Detail/List------------------
#TODO: CartItem API VIEWS
