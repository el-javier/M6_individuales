from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CustomUserForm(UserCreationForm):
    # pass
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
