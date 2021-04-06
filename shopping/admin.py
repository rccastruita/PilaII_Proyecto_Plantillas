from django.contrib import admin
from . import models as MyModels

# Register your models here.
admin.site.register(MyModels.ProductCategory)
admin.site.register(MyModels.Product)
admin.site.register(MyModels.ProductPresentation)