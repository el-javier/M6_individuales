from django.db import models
# from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Create your models here.

# # Crear el primer grupo
# grupo1, creado = Group.objects.get_or_create(name='Grupo1')

# # Crear el segundo grupo
# grupo2, creado = Group.objects.get_or_create(name='Grupo2')


# # Obtener el modelo en el que deseas asignar permisos
# Modelo = ContentType.objects.get(app_label='mi_app', model='mi_app_modelo')

# # Asignar permisos al primer grupo
# permiso1 = Permission.objects.create(codename='puede_hacer_algo1', name='Puede hacer algo 1', content_type=Modelo)
# grupo1.permissions.add(permiso1)

# # Asignar permisos al segundo grupo
# permiso2 = Permission.objects.create(codename='puede_hacer_algo2', name='Puede hacer algo 2', content_type=Modelo)
# grupo2.permissions.add(permiso2)
