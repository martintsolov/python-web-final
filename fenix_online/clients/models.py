from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ENTITY_FORMS = (
    ('EOOD', 'EOOD'),
    ('OOD', 'OOD'),
    ('AD', 'AD'),
    ('ET', 'ET'),
)


class Client(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    company_name = models.CharField(
        max_length=30,
        null=True,
    )
    company_form = models.CharField(
        max_length=5,
        choices=ENTITY_FORMS,
        default='EOOD',
    )
    address = models.CharField(
        max_length=250,
    )
    city = models.CharField(
        max_length=30,
    )
    postcode = models.CharField(
        max_length=4,
        validators=[
            RegexValidator('^\\d{4}$', 'Invalid postcode.')
        ]
    )
    eik_number = models.CharField(
        max_length=9,
        validators=[
            RegexValidator('^\\d{9}$', 'Wrong EIK number format.'),
        ]
    )
    vat_status = models.BooleanField(
        blank=True
    )
    vat_number = models.CharField(
        max_length=11,
        validators=[
            RegexValidator('^BG[0-9]{9}$', 'Wrong VAT number format.'),
        ],
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator('^\+359\d+$', 'Invalid phone number format.')
        ],
        null=True,
    )
