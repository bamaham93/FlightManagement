from django.db import models
# from customers.models import Order
from aircraft.models import Aircraft
from pilots.models import Pilot

# Create your models here.
class Flight(models.Model):
    """
    """
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)  # TODO
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    aircraft_assigned = models.ManyToManyField(Aircraft)  # TODO
    captain_assigned = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    first_officer_assigned = models.ForeignKey(Pilot, on_delete=models.CASCADE)

