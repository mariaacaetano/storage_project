import os

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.views import View

from .serializers import UserSerializer
from .models import CustomUser
from .forms import SignUpForm
from .db_helper import list_employee_info

from .utils import validate_user_data, get_user_response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.tokens import RefreshToken

class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user
        user_info = {
            "username": user.username,
            "email": user.email,
            "phone_number": user.phone_number,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "full_name": f"{user.first_name} {user.last_name}",
            "profile_photo": f"{user.profile_photo}",
            "role": user.role,
            "phone_number": user.phone_number,
            "registration": user.registration,
            "situation": user.situation,
            "permission": user.permission,
            "cpf": user.cpf,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,
        }
        return Response(user_info)

    def put(self, request, *args, **kwargs):
        user = request.user  # Usuário autenticado via JWT

        data = request.data
        updated_fields = {}

        if 'first_name' in data:
            updated_fields['first_name'] = data['first_name']
        if 'last_name' in data:
            updated_fields['last_name'] = data['last_name']
        if 'phone_number' in data:
            updated_fields['phone_number'] = data['phone_number']
        if 'role' in data:
            updated_fields['role'] = data['role']
        if 'registration' in data:
            updated_fields['registration'] = data['registration']
        if 'situation' in data:
            updated_fields['situation'] = data['situation']
        if 'cpf' in data:
            updated_fields['cpf'] = data['cpf']
        if 'is_staff' in data:
            updated_fields['is_staff'] = data['is_staff'] in ['true', 'True', True, 1]

        if 'profile_photo' in request.FILES:
            profile_photo = request.FILES['profile_photo']
            file_path = os.path.join('profile_pictures', profile_photo.name)
            path = default_storage.save(file_path, ContentFile(profile_photo.read()))
            updated_fields['profile_photo'] = path

        for field, value in updated_fields.items():
            setattr(user, field, value)

        user.save()

        return Response(
            {"message": "User information updated successfully"},
            status=status.HTTP_200_OK
        )

        
class CustomUserSignupView(APIView):
    permission_classes = [AllowAny]  # Permitir acesso público ao login

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Cadastro realizado com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomUserLoginView(APIView):
    permission_classes = [AllowAny]  # Permitir acesso público ao login

    def post(self, request):
        username = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)  # Autenticando via email
        print(f"Login attempt with email: {username} and password: {password}")

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"detail": f"Invalid credentials: {password} :: {username}"}, status=401)


class EmployeeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Lista todas as instâncias de CustomUser
        """
        employees = CustomUser.objects.all().values(
            "id", "first_name", "last_name", "email", "role",
            "phone_number", "registration","cpf",
            "profile_photo","situation","is_staff", "permission"
        )
        return JsonResponse(list(employees), safe=False)
    
    

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        # Verifica se o usuário é superusuário
        if request.user and request.user.is_superuser:
            return True
        raise PermissionDenied("Seu usuário não tem acesso a essa função.")

class EditEmployeeView(APIView):
    permission_classes = [IsSuperUser]
    
    def delete(self, request, id):
        try:
            # Substituir data_table por Employee (ou o nome correto do modelo)
            employee = CustomUser.objects.get(id=id)  # Buscar o funcionário
            employee.delete()  # Deletar o funcionário
            return Response({"message": "Funcionário deletado com sucesso!"}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "Funcionário não encontrado."}, status=status.HTTP_404_NOT_FOUND)


    def get(self, request, *args, **kwargs):
        """
        Retorna as informações de um funcionário específico pelo ID.
        """
        employee_id = kwargs.get('id')  # Pega o ID do funcionário pela URL
        try:
            employee = CustomUser.objects.get(id=employee_id)
            employee_info = {
                "first_name": employee.first_name,
                "last_name": employee.last_name,
                "full_name": f"{employee.first_name} {employee.last_name}",
                "email": employee.email,
                "phone_number": employee.phone_number,
                "role": employee.role,
                "registration": employee.registration,
                "permission": employee.permission,
                "situation": employee.situation,
                "cpf": employee.cpf,
                "profile_photo": employee.profile_photo.url if hasattr(employee.profile_photo, 'url') else None,
                "is_staff": employee.is_staff,
                "is_superuser": employee.is_superuser
            }
            return Response(employee_info)
        except CustomUser.DoesNotExist:
            return Response({"error": "Funcionário não encontrado"}, status=404)

    def put(self, request, id):
        try:
            employee = CustomUser.objects.get(id=id)
            # Atualiza os campos do funcionário
            employee.first_name = request.data.get('first_name', employee.first_name)
            employee.last_name = request.data.get('last_name', employee.last_name)
            employee.email = request.data.get('email', employee.email)
            employee.phone_number = request.data.get('phone_number', employee.phone_number)
            employee.role = request.data.get('role', employee.role)
            employee.registration = request.data.get('registration', employee.registration)
            employee.situation = request.data.get('situation', employee.situation)
            employee.permission = request.data.get('permission', employee.permission)
            employee.cpf = request.data.get('cpf', employee.cpf)

            # Verifica se há uma nova imagem
            if 'profile_photo' in request.data:
                picture = request.data.get('profile_photo', employee.profile_photo)
                employee.profile_photo = f"profile_pictures/{picture}"

            employee.save()
            return Response({'message': 'Dados atualizados com sucesso!'}, status=200)

        except Exception as e:
            return Response({'error': str(e)}, status=500)
