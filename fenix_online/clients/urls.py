from django.urls import path

from fenix_online.clients.views import client_login, client_register

urlpatterns = [
    # path('index/', view_home),
    path('login/', client_login, name='login'),
    path('register/', client_register, name='register'),
]
