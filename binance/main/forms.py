from django import forms
from django.forms import TextInput

from .models import CoinName, Comment 


class CoinForm(forms.ModelForm):
	class Meta:
		model = CoinName 
		fields = ('name', )
		widgets = {'name': TextInput(attrs={
			'class': 'input-coin',
			'name': 'coin',
			'id': 'coin',
			'placeholder': 'Enter coin'
			})}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment 
		fields = ('name', 'body', )