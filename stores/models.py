from django.db import models

class City(models.Model):
    name = models.CharField(max_length=40, default="Torreón")

    def __str__(self):
        return f"{self.name}"

class Store(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    name = models.CharField(max_length=40, default="Store")
    address = models.CharField(max_length=60, default="Calle 12 #123")
    zip_code = models.CharField(max_length=10, default="27123")
    phone_number = models.CharField(max_length=15, default="8711234567")
    email = models.EmailField(default="mymail@bakery.com")

    def __str__(self):
        return f"{self.pk}:{self.name}"