from django.contrib import admin
from . import models as my_models

# Register your models here.
admin.site.register(my_models.ProductCategory)
admin.site.register(my_models.Product)
admin.site.register(my_models.ProductPresentation)
admin.site.register(my_models.CartItem)