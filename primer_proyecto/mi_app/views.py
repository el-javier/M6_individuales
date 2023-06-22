from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate

# Create your views here.
def landing(request):
    return render(request, 'landing_page.html')

def usuarios(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'usuarios.html', context)

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autentificar al usuario y redirigirlo
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='usuarios')

    return render(request, 'registro.html', data)