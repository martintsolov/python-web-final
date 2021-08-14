from django.urls import path

from fenix_online.orders.views import create_order, list_orders, mark_order_as_full, client_edit_order, delete_order, \
    dump_and_return, admin_list_orders, admin_edit_order, admin_list_received_orders, admin_list_scheduled_orders, \
    admin_list_delivered_orders, admin_list_full_orders, admin_list_picked_orders

urlpatterns = [
    path('create_order/', create_order, name='create order'),
    path('list_orders/', list_orders, name='list orders'),
    path('cl_edit_order/<int:pk>', client_edit_order, name='client edit order'),
    path('delete_order/<int:pk>', delete_order, name='delete order'),
    path('full/<int:pk>', mark_order_as_full, name='mark full'),
    path('dump_return/<int:pk>', dump_and_return, name='dump and return'),
    path('all_orders/', admin_list_orders, name='admin list orders'),
    path('received/', admin_list_received_orders, name='admin list received'),
    path('scheduled/', admin_list_scheduled_orders, name='admin list scheduled'),
    path('delivered/', admin_list_delivered_orders, name='admin list delivered'),
    path('full/', admin_list_full_orders, name='admin list full'),
    path('pickedup/', admin_list_picked_orders, name='admin list picked'),
    path('update_order/<int:pk>', admin_edit_order, name='admin edit order'),
]