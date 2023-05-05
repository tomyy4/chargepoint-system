from django.db import models


class Status(models.TextChoices):
    READY = 'Ready', 'Ready'
    CHARGING = 'Charging', 'Charging'
    PENDING = 'Waiting', 'Waiting'
    ERROR = 'Error', 'Error'


class ChargePoint(models.Model):
    name = models.CharField(max_length=32, unique=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.READY)
    created_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)