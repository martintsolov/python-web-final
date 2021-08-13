from django import forms
from django.forms import SelectDateWidget, TimeInput

from fenix_online.containers.models import Container
from fenix_online.orders.models import Order
from fenix_online.trucks.models import Truck


class CreateOrderForm(forms.ModelForm):
    wanted_date = forms.DateField(widget=SelectDateWidget)
    class Meta:
        model = Order
        fields = ['container_size', 'wanted_date']


class ClientEditOrderForm(CreateOrderForm):
    pass


class AdminEditOrderForm(forms.ModelForm):
    container = forms.ModelChoiceField(
        queryset=Container.objects.filter(status=True)
    )
    delivered_by = forms.ModelChoiceField(
        queryset=Truck.objects.all()
    )
    wanted_date = forms.DateField(widget=SelectDateWidget)
    scheduled_for = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = Order
        fields = ['container_size', 'wanted_date', 'status', 'scheduled_for', 'delivered_by', 'container']


class DeleteOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['container_size', 'wanted_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
