from django import forms

from .models import Comment

# Form for posting and editing comments
class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'rating']
        labels = {
            'body': 'Comentario',
            'rating': 'Calificación',
        }
        widgets = {
            #'rating': forms.RadioSelect(attrs={'class': 'comment__stars-field'}),
            'rating': forms.HiddenInput,
        }
        