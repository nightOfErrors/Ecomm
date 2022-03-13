from home.models import ShippingAddress
from django import forms
from django.forms import ModelForm

class ShippingAddressForm(forms.ModelForm):
    
    class Meta:
        model = ShippingAddress
        fields = ['address', 'city', 'zipcode', 'state', 'country', 'order']

