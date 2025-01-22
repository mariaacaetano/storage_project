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

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Cadastro realizado com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(View):

    def post(self, request):
        data = request.POST
        user = authenticate(username=data['email'], password=data['password'])

        if user is None:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)

        login(request, user)
        return JsonResponse({'message': 'Logged in successfully'}, status=200)


class EmployeeView(View):
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
