from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication
from .serializers import UserSerializer, AddressSerializer
from customer.models import Address
from core.models import User
from .APIpermissions import UserCustomPerm

# Create your views here.
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [BasicAuthentication]


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserCustomPerm]
    authentication_classes = [BasicAuthentication]


class AddressListView(generics.ListAPIView):
    serializer_class = AddressSerializer
    # permission_classes = [IsOwner]
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        print(self.request.user)
        return Address.objects.filter(customer__user = self.request.user)

class AddressDetailView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [BasicAuthentication]
