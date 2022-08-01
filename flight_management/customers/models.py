from django.db import models

# Create your models here.
class Customer(models.Model):
    """
    """
    customer_name = models.CharField(max_length=50)


class Order(models.Model):
    """
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_made_date = models.DateTimeField()
