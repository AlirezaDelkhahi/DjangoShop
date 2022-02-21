from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
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
        form = UserRegistrationForm()
        return render(request, self.template_name, {'form': form})

