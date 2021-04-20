from django import forms

from .models import Comment

class CommentForm(forms.Form):
    body = forms.CharField(label='Deja un comentario', widget=forms.Textarea, required=True, strip=True)