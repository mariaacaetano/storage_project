from django.contrib import admin
from .models import PermissionType, CustomUser

# Registrar os modelos diretamente no Django Admin
admin.site.register(PermissionType)
admin.site.register(CustomUser)
