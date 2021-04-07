from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models as MyModels


# Register your models here.
class UserAdmin(BaseUserAdmin):
    model = MyModels.User

    list_display = (
        'username',
        'email',
        'city',
        'in_mailing_list',
    )
    
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

admin.site.register(MyModels.User, UserAdmin)