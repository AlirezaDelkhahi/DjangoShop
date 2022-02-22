from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from core.models import User
from django.contrib import messages

# Create your views here.


class UserRegisterView(View):
    template_name = 'customer/register.html'
    form = UserRegistrationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserRegistrationForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(phone=cd['phone'], email=cd['email'], password=cd['password1'])
            messages.success(request, 'you registered successfully', 'success')
            return redirect('product:home')
        else:
            print(form.errors)
            messages.error(request, 'ridi', 'danger')

            return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    template_name = 'customer/login.html'
    form = UserLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form()})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(request, username=clean_data['phone'], password=clean_data['password1'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('product:home')
            else:
                messages.error(request, 'username or password is not correct', 'danger')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "you've been logged out successfully", 'success')
        return redirect('product:home')
