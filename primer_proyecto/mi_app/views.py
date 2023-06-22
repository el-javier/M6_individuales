from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CustomUserForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required

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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@permission_required('mi_app.puede_ver_datos')
def restringido(request):
    # Código de la vista restringida
    return render(request, 'restricted.html')