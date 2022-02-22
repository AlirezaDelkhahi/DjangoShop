from django.urls import path, include
from .views import UserRegisterView
app_name = 'customer'

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='user-register')
]