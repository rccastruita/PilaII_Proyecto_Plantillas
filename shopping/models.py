from django.db import models
from gdstorage.storage import GoogleDriveStorage # Google Cloud media files

gd_storage = GoogleDriveStorage() # Cloud file manager initialization

class ProductCategory(models.Model):
    name = models.CharField(max_length=30, default='Category')
    description = models.TextField(default='')

    def __str__(self):
        return f"{self.pk}:{self.name}: {self.description[:20]}..."

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=30, default='Nombre_Producto')
    description = models.TextField(default='')
    image_1 = models.ImageField(upload_to='products', null=True, storage=gd_storage)

    def __str__(self):
        return f"{self.pk}:{self.name}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product_detail', args=[str(self.pk)])

class ProductPresentation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='Regular')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.pk}:{self.product.name} - {self.name}: ${self.price}"