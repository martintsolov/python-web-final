from django.db import models


class Truck(models.Model):
    reg_number = models.CharField(
        max_length=8,
    )
    brand = models.CharField(
        max_length=15
    )

    def __repr__(self):
        return f'{self.brand} {self.reg_number}'
