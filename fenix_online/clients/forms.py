from django import forms
from django.contrib.auth.models import User
from fenix_online.clients.models import Client


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class ClientForm(forms.ModelForm):
    vat_status = forms.BooleanField(label='VAT registered')
    vat_number = forms.CharField(label='VAT number')

    class Meta:
        model = Client
        fields = ['address', 'city', 'postcode', 'eik_number', 'vat_status', 'vat_number']
