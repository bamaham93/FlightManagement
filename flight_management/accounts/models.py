from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AccountProfile(models.Model):
    """
    Extension of default Django User model that is specific to this app.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
