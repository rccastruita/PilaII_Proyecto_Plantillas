from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.forms import ModelForm

from .models import User

class UserCreationForm(BaseUserCreationForm):
    """Form for user signup"""
    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

class UserChangeForm(ModelForm):
    """Form for updating the user info"""
    class Meta:
        model = User
        fields = ( # Fields to display
            'username',
            'email',
            'city',
            'in_mailing_list',
        )
        labels = { # Custom labels for fields to display
            'username': 'Nombre de usuario',
            'city': 'Ciudad',
            'in_mailing_list': 'Recibir correos con promociones',
        }