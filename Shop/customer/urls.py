from django.urls import path, include
from .views import UserRegisterView, UserLoginView
app_name = 'customer'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]