from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.
class PermissionType(models.Model):
    permission_id = models.AutoField(primary_key=True)
    permission = models.TextField()
    
    def __str__(self):
        return self.permission

class UserManager(auth_models.BaseUserManager):
    def create_user(self, first_name: str, last_name: str, email: str, password: str = None, is_staff=False, is_superuser=False) -> "CustomUser":
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user
    
    def create_superuser(self, first_name: str, last_name: str, email: str, password: str = None) -> "CustomUser":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        return user
    
class CustomUser(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    email = models.EmailField(verbose_name="Email", unique=True)
    password = models.CharField(max_length=255)
    username = None  # Não precisa de username, usamos o email como identificador único.
    state = models.TextField(default="Trabalhando")
    phone_number = models.TextField(default="4712345678")
    password = models.CharField(max_length=100)
    registration = models.IntegerField() 
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]  # Campos obrigatórios para a criação de um superusuário.

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
