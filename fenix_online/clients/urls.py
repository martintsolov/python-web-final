from django.urls import path

from fenix_online.clients.views import client_login, \
    client_register, home, client_logout, client_profile, edit_client_profile, delete_client_profile, \
    admin_list_clients, admin_edit_client_profile, admin_delete_client

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', client_login, name='login'),
    path('logout/', client_logout, name='logout'),
    path('register/', client_register, name='register'),
    path('profile/', client_profile, name='client profile'),
    path('edit_profile/', edit_client_profile, name='edit profile'),
    path('delete_profile/', delete_client_profile, name='delete profile'),
    path('list_clients/', admin_list_clients, name='admin list clients'),
    path('edit_client/<int:pk>', admin_edit_client_profile, name='admin edit client'),
    path('delete_client/<int:pk>', admin_delete_client, name='admin delete client'),
]
