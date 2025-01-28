from django.contrib import admin
from .models import PermissionType, CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
    )

# Registrar os modelos no Django Admin
admin.site.register(PermissionType)
admin.site.register(CustomUser, UserAdmin)
