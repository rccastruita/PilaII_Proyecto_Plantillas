from django.contrib import admin

from . import models as my_models

# Register your models here.
admin.site.register(my_models.City)
admin.site.register(my_models.Store)