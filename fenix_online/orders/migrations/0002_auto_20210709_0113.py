# Generated by Django 3.2.4 on 2021-07-08 22:13

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0001_initial'),
        ('trucks', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='container',
            field=models.ForeignKey(choices=[(1, Decimal('5.0'))], null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='containers.container'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivered_by',
            field=models.ForeignKey(choices=[], null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='trucks.truck'),
        ),
    ]
