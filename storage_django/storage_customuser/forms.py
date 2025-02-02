from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from .models import CustomUser

class SignUpForm(forms.Form):
    primeiro_nome = forms.CharField(max_length=100)
    ultimo_nome = forms.CharField(max_length=100)
    matricula = forms.CharField(max_length=10)
    cpf = forms.CharField(max_length=11)
    email = forms.EmailField(validators=[EmailValidator()])
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())  # Alterei o nome para seguir convenção
    telefone = forms.CharField(max_length=15, required=False)  # Telefones podem ser opcionais

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('password')
        confirmar_senha = cleaned_data.get('confirm_password')
        
        # Validação de senhas
        if senha != confirmar_senha:
            raise ValidationError('As senhas não coincidem.')
        
        # Validação de nome completo
        if not cleaned_data.get('primeiro_nome') or not cleaned_data.get('ultimo_nome'):
            raise ValidationError('Nome completo é necessário.')

        # Validação de matrícula (deve ser numérica e ter o tamanho adequado)
        matricula = cleaned_data.get('matricula')
        if not matricula.isdigit():
            raise ValidationError('A matrícula deve ser numérica.')
        if len(matricula) != 10:  # Exemplo: Caso a matrícula deva ter 10 caracteres
            raise ValidationError('A matrícula deve ter 10 dígitos.')

        # Validação de email (garantir que o email não esteja duplicado)
        email = cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('Este e-mail já está cadastrado.')

        return cleaned_data
