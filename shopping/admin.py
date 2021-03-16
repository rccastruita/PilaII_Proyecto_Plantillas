from django.contrib import admin
from . import models as MyModels

# Register your models here.
admin.site.register(MyModels.Categoria)
admin.site.register(MyModels.Producto)
admin.site.register(MyModels.Presentacion)
admin.site.register(MyModels.Sucursal)