from django.urls import path

from fenix_online.clients.views import client_login, \
    client_register, home, client_logout, client_profile, edit_client_profile, delete_client_profile, admin_list_clients

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', client_login, name='login'),
    path('logout/', client_logout, name='logout'),
    path('register/', client_register, name='register'),
    path('profile/', client_profile, name='client profile'),
    path('edit-profile/', edit_client_profile, name='edit profile'),
    path('delete-profile/', delete_client_profile, name='delete profile'),
    path('list-clients/', admin_list_clients, name='admin list clients'),
]
