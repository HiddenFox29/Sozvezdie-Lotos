from django import forms
from .models import Partners
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
	name = forms.CharField(required=True, label='Имя')
	email = forms.EmailField(required=True)
	text = forms.CharField(widget=forms.Textarea, required=True, label='Сообщение')

	class Meta:
		model = Partners
		fields = ['name', 'email', 'text']


