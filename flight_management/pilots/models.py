from django.db import models
# from flights.models import Flights TODO


# Create your models here.
class Pilot(models.Model):
    """
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Qualification(models.Model):
    """
    """
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    qualification_name = models.CharField(max_length=100)
    certificate_number = models.CharField(max_length=100, null=True, blank=True)
    certificate_description = models.TextField()
    certificate_expiration = models.DateField()
