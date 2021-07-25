from django.urls import path

from fenix_online.clients.views import client_login, \
    client_register, home, client_logout, client_profile

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', client_login, name='login'),
    path('logout/', client_logout, name='logout'),
    path('register/', client_register, name='register'),
    path('profile/', client_profile, name='client profile'),
]
