from django.db import models


class Container(models.Model):
    capacity = models.DecimalField(
        max_digits=6,
        decimal_places=1
    )
    status = models.BooleanField(default=True)

    def __repr__(self):
        return f"{self.id}, {self.capacity}"

    def __str__(self):
        return f"#{self.id}, cap. {self.capacity}m3"