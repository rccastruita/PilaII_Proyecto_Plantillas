from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    city = models.ForeignKey("stores.City", null=True, blank=True, on_delete=models.SET_NULL)
    in_mailing_list = models.BooleanField(default=True)