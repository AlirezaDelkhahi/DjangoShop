from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
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
