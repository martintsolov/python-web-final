from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Client(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    address = models.CharField(
        max_length=250,
    )
    city = models.CharField(
        max_length=30,
    )
    postcode = models.IntegerField()
    eik_number = models.IntegerField()
    vat_status = models.BooleanField()
    vat_number = models.CharField(
        max_length=11,
        validators=[
            RegexValidator('^BG[0-9]{9}$', 'Your VAT number must be in the following format: BG123456789'),
        ]
    )
