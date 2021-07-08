from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fenix_online.clients.urls')),
    path('', include('fenix_online.containers.urls')),
    path('', include('fenix_online.orders.urls')),
    path('', include('fenix_online.trucks.urls')),
    # path('about/', about_us, name='about page')
]
