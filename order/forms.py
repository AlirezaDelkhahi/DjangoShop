from django import forms
from customer.models import Address, Customer
class AddressForm(forms.Form):
    address = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class':'form-select'}), label='')

    def __init__(self, customer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].queryset = Address.objects.filter(customer=customer)