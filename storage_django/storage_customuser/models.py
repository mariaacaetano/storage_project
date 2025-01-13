from django.db import models

# Create your models here.
class PermissionType(models.Model):
    permission_id = models.AutoField(primary_key=True)
    permission = models.TextField()
    
    def __str__ (self):
        return self.permission


class CustomUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    matricula = models.IntegerField()               
    primeiro_nome = models.CharField(max_length=100)               
    ultimo_nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    situacao = models.TextField(default="Trabalhando")
    telefone = models.TextField(default="4712345678")
    password = models.CharField(max_length=100)
    permission = models.ForeignKey(PermissionType, on_delete=models.CASCADE, null=True)
    