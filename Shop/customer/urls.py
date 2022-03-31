from django.urls import path, include
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserPasswordResetView, UserPasswordResetDoneView, \
    UserPasswordResetConfirmView, UserPasswordResetCompleteView, PanelView

app_name = 'customer'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('reset/', UserPasswordResetView.as_view(), name='reset_password'),
    path('reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/complete', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('panel', PanelView.as_view(), name='panel'),
    
]