from django.urls import path

from fenix_online.orders.views import create_order, list_orders, mark_order_as_full, client_edit_order, delete_order, \
    dump_and_return

urlpatterns = [
    path('create_order/', create_order, name='create order'),
    path('list_orders/', list_orders, name='list orders'),
    path('cl_edit_order/<int:pk>', client_edit_order, name='client edit order'),
    path('delete_order/<int:pk>', delete_order, name='delete order'),
    path('full/<int:pk>', mark_order_as_full, name='mark full'),
    path('dump_return/<int:pk>', dump_and_return, name='dump and return'),
]