from django.db import models


class Doctor(models.Model):

    name = models.CharField(
        max_length=150
    )

    specialization = models.CharField(
        max_length=150
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.specialization}"