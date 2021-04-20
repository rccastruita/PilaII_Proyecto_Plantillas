from django import forms

from .models import Comment

class CommentForm(forms.Form):
    body = forms.CharField(
        label='Deja un comentario', 
        required=True, strip=True,
        widget=forms.Textarea(attrs={'cols': 200}),
    )

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': 'Editar'
        }