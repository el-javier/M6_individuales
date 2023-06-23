from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group



# class CustomUserForm(UserCreationForm):
#     # pass
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2']

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        exclude = ['groups']

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()

        group_name = 'usuarios'
        group = Group.objects.get(name=group_name)
        user.groups.add(group)

        return user



class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

# class NewUserForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput())
#     groups = forms.ModelChoiceField(queryset=Group.objects.all())

#     def save(self):
#         user = User.objects.usuario_grupo(
#             username=self.cleaned_data['username'],
#             email=self.cleaned_data['email'],
#             password=self.cleaned_data['password']
#         )
#         group = self.cleaned_data['groups']
#         user.groups.add(group)
#         return user


class NewUserForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    groups = forms.ModelChoiceField(queryset=Group.objects.all())

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Las contraseñas no coinciden.')

    def save(self):
        username = self.cleaned_data['username']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        group = self.cleaned_data['groups']

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.groups.add(group)
        return user
