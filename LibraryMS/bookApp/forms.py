from bookApp.models import Book
from cProfile import label
from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUser(UserCreationForm):
	email = forms.EmailField(required=True)
	password2=forms.CharField(label='Confirm Password',
	widget=forms.PasswordInput)
	class Meta:
		model = User
		fields=['username','first_name','last_name','email']
		labels={'email':'Email'}

class AddBookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields="__all__"
		widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "date":forms.DateInput(attrs={"class":"form-control"}),
        }