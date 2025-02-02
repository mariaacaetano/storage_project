from django.db import models
from django.contrib.auth import models as auth_models

class UserManager(auth_models.BaseUserManager):
    def create_user(self, first_name: str, last_name: str, email: str, password: str = None, is_staff=False, is_superuser=False) -> "CustomUser":
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name: str, last_name: str, email: str, password: str = None) -> "CustomUser":
        return self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )

class CustomUser(auth_models.AbstractUser):
    PERMISSION_CHOICES = [
        ('ADMINISTRADOR', 'Administrador'),
        ('SOMENTE LEITURA', 'Somente Leitura'),
    ]
    permission = models.CharField(max_length=20, choices=PERMISSION_CHOICES, default='Somente Leitura')
    username = None  # Removemos o username e usamos o email como identificador único.
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    email = models.EmailField(verbose_name="Email", unique=True)
    cpf = models.CharField(max_length=14, default="000.000.000-00")  # Formato correto de CPF
    role = models.CharField(max_length=50, default="Vendedor")
    phone_number = models.CharField(max_length=20, default="4712345678")
    registration = models.IntegerField(null=True, blank=True)  # Permite valores nulos para evitar erro
    profile_photo = models.CharField(max_length=255, null=True, blank=True)
    situation = models.TextField(default="Trabalhando")
    
    is_staff = models.BooleanField(default=True)  # Removida a vírgula
    is_superuser = models.BooleanField(default=False)  # Removida a vírgula

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    def save(self, *args, **kwargs):
        # Verificando a permissão selecionada e atualizando os campos relacionados
        if self.permission == 'Administrador':
            self.is_staff = True
            self.is_superuser = True
        elif self.permission == 'Somente Leitura':
            self.is_staff = True
            self.is_superuser = False
        else:
            # Se for outro valor de permissão, podemos definir o comportamento padrão
            self.is_staff = False
            self.is_superuser = False

        # Chama o método save do Django para salvar os dados no banco
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
