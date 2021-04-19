from django.core import validators
from django import forms
from .models import ContactBook

class ContactRegistration(forms.ModelForm):
 class Meta:
  model = ContactBook
  fields = ['name', 'email', 'number','address']
  widgets = {
   'name': forms.TextInput(attrs={'class':'form-control'}),
   'email': forms.EmailInput(attrs={'class':'form-control'}),
   'number': forms.TextInput(attrs={'class':'form-control'}),
   'address': forms.TextInput(attrs={'class':'form-control'}),
  
  }