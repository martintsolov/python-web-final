# Generated by Django 3.2.4 on 2021-07-08 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210709_0113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='owner',
        ),
    ]
