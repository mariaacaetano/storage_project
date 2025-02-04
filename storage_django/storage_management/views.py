from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Produto, Categoria, Fornecedor
from storage_customuser.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProdutoSerializer
from rest_framework.response import Response




# ---------------------------------------------
# ------------- PERMISSIONS -------------------
# ---------------------------------------------

def is_superuser(user):
    if user and user.is_superuser:
        return True
    raise PermissionDenied("Seu usuário não tem acesso a essa função.")


# ---------------------------------------------
# ---------------- PRODUTOS -------------------
# ---------------------------------------------
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Categoria, Fornecedor, Produto

@api_view(['POST'])
def create_produto(request):
    # Verificação do token de autenticação
    token = request.headers.get('Authorization')
    if not token or not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)
    
    data = request.data

    # Tentando encontrar a categoria
    try:
        categoria = Categoria.objects.get(id_categoria=data.get('categoria'))  # Usando 'id' no filtro
    except Categoria.DoesNotExist:
        return JsonResponse({'error': 'Categoria não encontrada'}, status=404)
    
    # Tentando encontrar o fornecedor
    try:
        fornecedor = Fornecedor.objects.get(id_fornecedor=data.get('fornecedor'))  # Usando 'id' no filtro
    except Fornecedor.DoesNotExist:
        return JsonResponse({'error': 'Fornecedor não encontrado'}, status=404)

    # Criando o produto
    produto = Produto.objects.create(
        nome_produto=data.get('nome_produto'),
        codigo_produto=data.get('codigo_produto'),
        preco_produto=data.get('preco_produto'),
        quantidade=data.get('quantidade'),
        status=True if data.get('status') == 'ativo' else False,
        categoria=categoria,
        fornecedor=fornecedor
    )

    # Retornando a resposta com sucesso e os detalhes do produto
    return JsonResponse({
        'id_produto': produto.id_produto,
        'message': 'Produto criado com sucesso!',
        'produto': {
            'nome_produto': produto.nome_produto,
            'codigo_produto': produto.codigo_produto,
            'preco_produto': produto.preco_produto,
            'quantidade': produto.quantidade,
            'status': produto.status,
            'categoria': produto.categoria.nome,
            'fornecedor': produto.fornecedor.nome_fantasia if produto.fornecedor.nome_fantasia else produto.fornecedor.nome
        }
    }, status=status.HTTP_201_CREATED)




@api_view(['GET'])
def list_produtos(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    produtos = Produto.objects.all()
    serializer = ProdutoSerializer(produtos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_produto(request, produto_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        produto = Produto.objects.get(id_produto=produto_id)
    except Produto.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)

    return JsonResponse({
        'id': produto.id_produto,
        'nome_produto': produto.nome_produto,
        'categoria': produto.categoria_id,
        'quantidade': produto.quantidade,
        'codigo_produto': produto.codigo_produto,
        'preco_produto': produto.preco_produto,
        'status': produto.status
    })


@api_view(['PUT'])
def update_produto(request, produto_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        produto = Produto.objects.get(id_produto=produto_id)
    except Produto.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)

    data = request.data
    produto.nome_produto = data.get('nome_produto', produto.nome_produto)
    produto.categoria_id = data.get('categoria', produto.categoria_id)
    produto.quantidade = data.get('quantidade', produto.quantidade)
    produto.codigo_produto = data.get('codigo_produto', produto.codigo_produto)
    produto.preco_produto = data.get('preco_produto', produto.preco_produto)
    produto.status = data.get('status', produto.status)
    produto.save()

    return JsonResponse({'message': 'Produto atualizado com sucesso!'}, status=200)


@api_view(['DELETE'])
def delete_produto(request, produto_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        produto = Produto.objects.get(id_produto=produto_id)
    except Produto.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)

    produto.delete()
    return JsonResponse({'message': 'Produto excluído com sucesso!'}, status=200)


# ---------------------------------------------
# ------------- FORNECEDORES ------------------
# ---------------------------------------------


@api_view(['POST'])
def create_fornecedor(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    data = request.data
    fornecedor = Fornecedor.objects.create(
        razao_social=data.get('razao_social'),
        nome_fantasia=data.get('nome_fantasia'),
        cnpj=data.get('cnpj'),
        inscricao_estadual=data.get('inscricao_estadual'),
        telefone=data.get('telefone'),
        endereco=data.get('endereco'),
        tipo_produto=data.get('tipo_produto')
    )
    return JsonResponse({'id': fornecedor.pk, 'message': 'Fornecedor criado com sucesso!'}, status=201)


@api_view(['GET'])
def list_fornecedores(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    fornecedores = Fornecedor.objects.all()
    return JsonResponse(list(fornecedores.values()), safe=False)

@api_view(['PUT'])
def update_fornecedor(request, id_fornecedor):  # Alterado de `id` para `id_fornecedor`
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        fornecedor = Fornecedor.objects.get(id_fornecedor=id_fornecedor)  # Usar `id_fornecedor`
    except Fornecedor.DoesNotExist:
        return JsonResponse({'error': 'Fornecedor não encontrado'}, status=404)

    data = request.data
    fornecedor.razao_social = data.get('razao_social', fornecedor.razao_social)
    fornecedor.nome_fantasia = data.get('nome_fantasia', fornecedor.nome_fantasia)
    fornecedor.cnpj = data.get('cnpj', fornecedor.cnpj)
    fornecedor.inscricao_estadual = data.get('inscricao_estadual', fornecedor.inscricao_estadual)
    fornecedor.telefone = data.get('telefone', fornecedor.telefone)
    fornecedor.endereco = data.get('endereco', fornecedor.endereco)
    fornecedor.tipo_produto = data.get('tipo_produto', fornecedor.tipo_produto)
    fornecedor.save()

    return JsonResponse({'message': 'Fornecedor atualizado com sucesso!'}, status=200)



@api_view(['GET'])
def get_fornecedor(request, id_fornecedor):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        fornecedor = Fornecedor.objects.get(id_fornecedor=id_fornecedor)
    except Fornecedor.DoesNotExist:
        return JsonResponse({'error': 'Fornecedor não encontrado'}, status=404)

    return JsonResponse({
        'id_fornecedor': fornecedor.id_fornecedor,
        'razao_social': fornecedor.razao_social,
        'nome_fantasia': fornecedor.nome_fantasia,
        'cnpj': fornecedor.cnpj,
        'inscricao_estadual': fornecedor.inscricao_estadual,
        'telefone': fornecedor.telefone,
        'endereco': fornecedor.endereco,
        'tipo_produto': fornecedor.tipo_produto
    })



@api_view(['DELETE'])
def delete_fornecedor(request, id_fornecedor):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        fornecedor = Fornecedor.objects.get(id_fornecedor=id_fornecedor)
    except Fornecedor.DoesNotExist:
        return JsonResponse({'error': 'Fornecedor não encontrado'}, status=404)

    fornecedor.delete()
    return JsonResponse({'message': 'Fornecedor excluído com sucesso!'}, status=200)


# ---------------------------------------------
# ------------- CATEGORIAS --------------------
# ---------------------------------------------


@api_view(['POST'])
def create_categoria(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    data = request.data
    categoria = Categoria.objects.create(
        nome=data.get('nome'),
        descricao_categoria=data.get('descricao_categoria'),
        localizacao=data.get('localizacao')
    )
    return JsonResponse({'id': categoria.pk, 'message': 'Categoria criada com sucesso!'}, status=201)


@api_view(['GET'])
def list_categorias(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    categorias = Categoria.objects.all()
    return JsonResponse(list(categorias.values()), safe=False)


def categoria_detail(request, id):
    try:
        categoria = Categoria.objects.get(id_categoria=id)
        return JsonResponse({'nome': categoria.nome, 'descricao_categoria': categoria.descricao_categoria, 'localizacao': categoria.localizacao})
    except Categoria.DoesNotExist:
        return JsonResponse({'error': 'Categoria não encontrada'}, status=404)


@csrf_exempt
@api_view(['PUT'])
def update_categoria(request, categoria_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        categoria = Categoria.objects.get(id_categoria=categoria_id)
    except Categoria.DoesNotExist:
        return JsonResponse({'error': 'Categoria não encontrada'}, status=404)

    data = request.data
    categoria.nome = data.get('nome', categoria.nome)
    categoria.descricao_categoria = data.get('descricao_categoria', categoria.descricao_categoria)
    categoria.localizacao = data.get('localizacao', categoria.localizacao)
    categoria.save()

    return JsonResponse({'message': 'Categoria atualizada com sucesso!'}, status=200)


@api_view(['DELETE'])
def delete_categoria(request, categoria_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        categoria = Categoria.objects.get(id_categoria=categoria_id)
    except Categoria.DoesNotExist:
        return JsonResponse({'error': 'Categoria não encontrada'}, status=404)

    categoria.delete()
    return JsonResponse({'message': 'Categoria excluída com sucesso!'}, status=200)


@api_view(['GET'])
def get_categoria(request, categoria_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        categoria = Categoria.objects.get(id_categoria=categoria_id)
    except Categoria.DoesNotExist:
        return JsonResponse({'error': 'Categoria não encontrada'}, status=404)

    return JsonResponse({
        'id': categoria.categoria_id,
        'nome': categoria.nome,
        'descricao_categoria': categoria.descricao_categoria,
        'localizacao': categoria.localizacao
    })


# ---------------------------------------------
# ------------- SEARCH BAR --------------------
# ---------------------------------------------


@api_view(['GET'])
def search(request):
    query = request.GET.get('query', '')  # Recebe o parâmetro de busca 'query'
    
    # Buscando nas tabelas
    data = {
        'Produtos': list(Produto.objects.filter(nome_produto__icontains=query).values()),
        'Categorias': list(Categoria.objects.filter(descricao_categoria__icontains=query).values()),
        'Fornecedores': list(Fornecedor.objects.filter(nome_fantasia__icontains=query).values()),
        'Funcionários': list(CustomUser.objects.filter(primeiro_nome__icontains=query).values()),
    }
    
    return JsonResponse(data, safe=False)
