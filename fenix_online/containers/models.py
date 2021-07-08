from django.db import models


class Container(models.Model):
    capacity = models.DecimalField(
        max_digits=6,
        decimal_places=1
    )
    status = models.BooleanField(default=True)
