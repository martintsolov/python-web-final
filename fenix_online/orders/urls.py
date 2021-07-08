from django.urls import path

from fenix_online.orders.views import create_order

urlpatterns = [
    path('create_order/', create_order, name='create order')
]