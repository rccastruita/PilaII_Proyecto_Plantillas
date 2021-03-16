from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30, default='Nombre_Categoria')
    descripcion = models.TextField(default='Descripcion_Categoria')

    def __str__(self):
        return f"{self.id} - {self.nombre}: {self.descripcion[:20]}..."

class Producto(models.Model):
    nombre = models.CharField(max_length=30, default='Nombre_Producto')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    descripcion = models.TextField(default="Descripcion_Producto")
    imagen_1 = models.ImageField(upload_to='models/producto/images', null=True)

    def __str__(self):
        return f"{self.nombre} - {self.descripcion[:30]}..."

class Presentacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    detalle = models.CharField(max_length=30, default='Detalle_Presentacion')
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} - {self.detalle}: ${self.precio}"

class Sucursal(models.Model):
    nombre = models.CharField(max_length=40, default='Nombre_Sucursal')
    direccion = models.CharField(max_length=60, default='Direccion_Sucursal')
    colonia = models.CharField(max_length=40, default='Colonia_Sucursal')
    codigo_postal = models.CharField(max_length=10, default='27123')
    telefono = models.CharField(max_length=15, default='8711234567')
    email = models.EmailField(default='mymail@bakery.com')

    def __str__(self):
        return f"{self.nombre}"