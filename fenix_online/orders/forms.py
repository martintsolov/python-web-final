from django import forms
from django.forms import SelectDateWidget

from fenix_online.orders.models import Order


class CreateOrderForm(forms.ModelForm):
    wanted_date = forms.DateField(widget=SelectDateWidget)
    class Meta:
        model = Order
        fields = ['container_size', 'wanted_date']


class ClientEditOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['container_size', 'wanted_date']


class AdminEditOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class DeleteOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['container_size', 'wanted_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
