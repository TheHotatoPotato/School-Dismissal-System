from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class RegisterParentForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }

class CreateChildForm(ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'age', 'school', 'grade', 'section']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'school': forms.Select(attrs={'placeholder': 'School'}),
            'grade': forms.NumberInput(attrs={'placeholder': 'Grade'}),
            'section': forms.TextInput(attrs={'placeholder': 'Section'}),
        }