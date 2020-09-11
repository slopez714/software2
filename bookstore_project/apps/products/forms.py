from django import forms
from django.forms.forms import NON_FIELD_ERRORS

class SearchBookBasicForm(forms.Form):
	string_search = forms.CharField(required=False, label='Ingrese el nombre del autor o del título del libro', widget=forms.TextInput(attrs={'class': 'form-control',}))

class SearchBookComplexForm(forms.Form):
	string_search_author = forms.CharField(required=False, label='Autor', widget=forms.TextInput(attrs={'class': 'form-control',}))
	string_search_title = forms.CharField(required=False, label='Título', widget=forms.TextInput(attrs={'class': 'form-control',}))
	string_search_isbn = forms.IntegerField(required=False, label='ISBN', widget=forms.NumberInput(attrs={'class': 'form-control',}))