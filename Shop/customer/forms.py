from django import forms
from core.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    gender_choices = (
        ('male', 'مذکر'),
        ('female', 'مونث')
    )
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(phone=phone).exists():
            raise ValidationError('This Phone Number already exists !')
        else:
            return phone

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('This Username already exists !')
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(username=email).exists():
            raise ValidationError('This Email already exists !')
        else:
            return email

    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password1')
        confirm = clean_data.get('password2')

        if password and confirm and password != confirm:
            raise ValidationError('Password is not match !')