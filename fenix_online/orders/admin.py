from django.contrib import admin

# Register your models here.
from fenix_online.orders.models import Order

admin.site.register(Order)