from pyexpat import model
from django import forms
from .models import Coment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Coment
        exclude = ['creare_at', 'post']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Введите имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите email'}),
            'website': forms.TextInput(attrs={'placeholder': 'Введите название сайта'}),
            'message': forms.Textarea(attrs={'placeholder': 'Введите сообщение'})
        }