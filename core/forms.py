from django import forms
from core.models import comic, publisher, Coment

class comicForm(forms.ModelForm):
	class Meta:
		model= comic
		exclude=('exclude') 

class publisherForm(forms.ModelForm):
	class Meta:
		model=publisher
		exclude=('exclude')

class comentForm(forms.ModelForm):
	class Meta:
		model=Coment