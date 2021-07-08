# Generated by Django 3.2.4 on 2021-07-08 21:02

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trucks', '0001_initial'),
        ('containers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Received', 'Received'), ('Scheduled', 'Scheduled'), ('Delivered', 'Delivered'), ('Full', 'Full'), ('Picked-up', 'Picked-up')], default='Received', max_length=15)),
                ('container_size', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], default='Medium', max_length=15)),
                ('wanted_date', models.DateField()),
                ('container', models.ForeignKey(choices=[(1, Decimal('5.0'))], on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='containers.container')),
                ('delivered_by', models.ForeignKey(choices=[], on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='trucks.truck')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
