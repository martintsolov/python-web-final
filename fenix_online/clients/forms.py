from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator

from fenix_online.clients.models import Client


class UserForm(forms.ModelForm):
    email = forms.CharField(validators=[EmailValidator],
                            widget=forms.TextInput(attrs={'placeholder': 'example@gmail.com'}))
    username = forms.CharField(validators=[UnicodeUsernameValidator],
                               widget=forms.TextInput())

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class ClientForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g.: Ovoshtarska 5'}))
    postcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '4-digit postcode'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g.: +35912345678'}))
    vat_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'BG123456789'}))

    class Meta:
        model = Client
        fields = ['company_name', 'company_form',
                  'address', 'city', 'postcode',
                  'eik_number', 'vat_status', 'vat_number', 'phone_number']
