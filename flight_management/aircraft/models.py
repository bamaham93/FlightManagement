from django.db import models
# from flights.models import Flights

# Create your models here.
class Aircraft(models.Model):
    registration_number = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    # flights = models.ManyToManyField(Flights)  # TODO