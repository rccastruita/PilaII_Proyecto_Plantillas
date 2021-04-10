from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """Custom User model"""
    # Override field to be not null
    email = models.EmailField(null=False, unique=True)
    # Used for displaying stores in the same city as the user
    city = models.ForeignKey("stores.City", null=True, blank=True, on_delete=models.SET_NULL)
    # Used to receive emails with discounts
    in_mailing_list = models.BooleanField(default=True)