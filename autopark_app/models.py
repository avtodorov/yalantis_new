from django.db import models
from .validator import validate_plate


# Create your models here.
class Driver(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Vehicle(models.Model):
    driver_id = models.ForeignKey(Driver, null=True, blank=True, on_delete=models.SET_NULL)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    plate_number = models.CharField(
        max_length=10,
        validators=[validate_plate])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.model}, {self.plate_number}'
