from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.views import View
from .models import CustomUser
from .forms import SignUpForm
from .utils import validate_user_data, get_user_response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user  # Usuário autenticado via JWT
        user_info = {
            "username": user.username,
            "email": user.email,
            "phone_number": user.phone_number,
            "full_name": f"{user.first_name} {user.last_name}",
            # Outras informações do usuário podem ser retornadas aqui
        }
        return Response(user_info)
    
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

    data_table = CustomUser  # Define a tabela usada pela classe

    def get(self, request):
        """Lista todas as instâncias de CustomUser"""
        objects = self.data_table.objects.all()
        return JsonResponse(list(objects.values()), safe=False)

    def post(self, request):
        """Cria uma nova instância de CustomUser"""
        data = request.POST
        instance = self.data_table.objects.create(
            matricula=data['matricula'],
            primeiro_nome=data['primeiro_nome'],
            ultimo_nome=data['ultimo_nome'],
            email=data['email'],
            telefone=data.get('telefone', '4712345678'),
            situacao=data.get('situacao', 'Trabalhando'),
            password=data['password']
        )
        return JsonResponse({'id': instance.user_id, 'message': 'Employee created'}, status=201)

    def delete(self, request):
        """Deleta uma instância de CustomUser"""
        obj_id = request.POST.get('id')
        self.data_table.objects.filter(user_id=obj_id).delete()
        return JsonResponse({'message': 'Deleted successfully'}, status=200)

    def put(self, request):
        """Atualiza uma instância de CustomUser"""
        obj_id = request.POST.get('id')
        data = request.POST.dict()  # Converte QueryDict para dict
        data.pop('id', None)  # Remove o ID do dicionário para evitar problemas no update
        obj = self.data_table.objects.filter(user_id=obj_id).update(**data)
        if obj:
            return JsonResponse({'message': 'Updated successfully'}, status=200)
        return JsonResponse({'error': 'User not found'}, status=404)

    def read(self, request):
        """Lê uma instância específica de CustomUser"""
        obj_id = request.GET.get('id')
        obj = self.data_table.objects.filter(user_id=obj_id).values()
        if not obj:
            return JsonResponse({'error': 'Not found'}, status=404)
        return JsonResponse(list(obj)[0], safe=False)
