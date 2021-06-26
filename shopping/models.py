from django.db import models
from gdstorage.storage import GoogleDriveStorage # Google Cloud media files
from django.urls import reverse
from django.conf import settings
import time

gd_storage = GoogleDriveStorage() # Cloud file manager initialization

class ProductCategory(models.Model):
    """ Category for a product """
    name = models.CharField(max_length=30, default='Category')
    description = models.TextField(default='')

    def __str__(self):
        return f"{self.pk}:{self.name}: {self.description[:20]}..."

def product_image_path(instance, filename):
    """Creates a dynamic filename for Product.image"""
    return f"products/{instance.name}_{time.strftime('%Y%m%d%H%M%S')}{filename[-4:]}"

class Product(models.Model):
    """ Product to display on the catalog """
    category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30, default='Nombre_Producto')
    description = models.TextField(default='')
    image = models.ImageField(upload_to=product_image_path, null=True, blank=True, storage=gd_storage)

    def __str__(self):
        return f"{self.pk}:{self.name}"

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_pk':self.pk})

    # Url for the CommentCreateView of a specific product
    def get_new_comment_url(self):
        return reverse('comment_create', kwargs={'product_pk':self.pk})

class ProductPresentation(models.Model):
    """ Size or form of selling the product (small/big, 100gr, slice, etc.) """
    product = models.ForeignKey(Product, related_name='presentations', on_delete=models.PROTECT)
    name = models.CharField(max_length=30, default='Regular')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.pk}:{self.product.name} - {self.name}: ${self.price}"

class CartItem(models.Model):
    """ Item in a shopping cart """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='shopping_cart', on_delete=models.CASCADE)
    presentation = models.ForeignKey(ProductPresentation, on_delete=models.PROTECT)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.presentation.product.name} {self.presentation.name}"