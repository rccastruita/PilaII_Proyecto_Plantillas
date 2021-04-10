from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models as my_models
from . import forms as my_forms

# Register your models here.
class UserAdmin(BaseUserAdmin):
    model = my_models.User
    
    # Fields to display on the list view
    list_display = (
        'username',
        'email',
        'city',
        'in_mailing_list',
    )

    # Fields to display on change form
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
            )
        }),
        ("Personal info", {
            'fields': (
                'email',
                'first_name',
                'last_name',
                'city', 
                'in_mailing_list',
            )
        }),
        ("Important dates", {
            'fields': (
                'date_joined',
                'last_login',
            )
        }),
        ("Permissions", {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        })
    )

admin.site.register(my_models.User, UserAdmin)