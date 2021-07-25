from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.http import request

from fenix_online.containers.models import Container
from fenix_online.trucks.models import Truck


ORDER_STATUSES = (
    ('Received', 'Received'),
    ('Scheduled', 'Scheduled'),
    ('Delivered', 'Delivered'),
    ('Full', 'Full'),
    ('Picked-up', 'Picked-up')
)
CONTAINER_SIZES = (
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
)


class Order(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        default='Received',
        choices=ORDER_STATUSES,
        max_length=15,
    )
    container = models.ForeignKey(
        Container,
        on_delete=models.PROTECT,
        related_name='orders',
        null=True,
    )
    container_size = models.CharField(
        max_length=15,
        choices=CONTAINER_SIZES,
        default='Medium'
    )
    wanted_date = models.DateField()
    scheduled_for = models.DateTimeField(null=True)
    delivered_by = models.ForeignKey(
        Truck,
        on_delete=models.PROTECT,
        related_name='orders',
        null=True,
    )