from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def landing(request):
    return render(request, 'landing_page.html')

def usuarios(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'usuarios.html', context)




