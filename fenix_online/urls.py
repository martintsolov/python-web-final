from django.contrib import admin
from django.urls import path, include

from fenix_online.views import about_us_page, contact_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fenix_online.clients.urls')),
    path('', include('fenix_online.containers.urls')),
    path('', include('fenix_online.orders.urls')),
    path('', include('fenix_online.trucks.urls')),
    path('about/', about_us_page, name='about'),
    path('contact/', contact_page, name='contact'),
]
