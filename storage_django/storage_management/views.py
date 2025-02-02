from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Produto, Categoria, Fornecedor
from storage_customuser.models import CustomUser

def is_superuser(user):
    if user and user.is_superuser:
        return True
    raise PermissionDenied("Seu usuário não tem acesso a essa função.")

@api_view(['POST'])
def create_produto(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)
    
    data = request.data

    # Busca a Categoria e o Fornecedor pelos IDs fornecidos
    try:
        categoria = Categoria.objects.get(id=data.get('categoria'))
    except Categoria.DoesNotExist:
        return JsonResponse({'error': 'Categoria não encontrada'}, status=404)
    
    try:
        fornecedor = Fornecedor.objects.get(id=data.get('fornecedor'))
    except Fornecedor.DoesNotExist:
        return JsonResponse({'error': 'Fornecedor não encontrado'}, status=404)

    # Criação do Produto com relações corretas
    produto = Produto.objects.create(
        nome_produto=data.get('nome_produto'),
        categoria=categoria,  # Associa objeto Categoria
        fornecedor=fornecedor,  # Associa objeto Fornecedor
        quantidade=data.get('quantidade'),
        codigo_produto=data.get('codigo_produto'),
        preco_produto=data.get('preco_produto'),
        status=data.get('status', True)
    )

    return JsonResponse({
        'id': produto.pk,
        'message': 'Produto criado com sucesso!',
        'produto': {
            'nome': produto.nome_produto,
            'categoria': produto.categoria.nome,
            'fornecedor': produto.fornecedor.nome_fantasia,
            'quantidade': produto.quantidade,
            'codigo_produto': produto.codigo_produto,
            'preco_produto': produto.preco_produto,
            'status': produto.status
        }
    }, status=201)


@api_view(['GET'])
def list_produtos(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)
    
    produtos = Produto.objects.all()
    return JsonResponse(list(produtos.values()), safe=False)

@api_view(['GET'])
def get_produto(request, produto_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        produto = Produto.objects.get(id=produto_id)
    except Produto.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)

    return JsonResponse({
        'id': produto.id,
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
        produto = Produto.objects.get(id=produto_id)
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
        produto = Produto.objects.get(id=produto_id)
    except Produto.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)

    produto.delete()
    return JsonResponse({'message': 'Produto excluído com sucesso!'}, status=200)

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
def update_fornecedor(request, fornecedor_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
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
def get_fornecedor(request, fornecedor_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
    except Fornecedor.DoesNotExist:
        return JsonResponse({'error': 'Fornecedor não encontrado'}, status=404)

    return JsonResponse({
        'id': fornecedor.id,
        'razao_social': fornecedor.razao_social,
        'nome_fantasia': fornecedor.nome_fantasia,
        'cnpj': fornecedor.cnpj,
        'inscricao_estadual': fornecedor.inscricao_estadual,
        'telefone': fornecedor.telefone,
        'endereco': fornecedor.endereco,
        'tipo_produto': fornecedor.tipo_produto
    })


@api_view(['DELETE'])
def delete_fornecedor(request, fornecedor_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
    except Fornecedor.DoesNotExist:
        return JsonResponse({'error': 'Fornecedor não encontrado'}, status=404)

    fornecedor.delete()
    return JsonResponse({'message': 'Fornecedor excluído com sucesso!'}, status=200)

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
        categoria = Categoria.objects.get(id=id)
        return JsonResponse({'nome': categoria.nome, 'descricao_categoria': categoria.descricao_categoria, 'localizacao': categoria.localizacao})
    except Categoria.DoesNotExist:
        return JsonResponse({'error': 'Categoria não encontrada'}, status=404)


@api_view(['PUT'])
def update_categoria(request, categoria_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        categoria = Categoria.objects.get(id=categoria_id)
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
        categoria = Categoria.objects.get(id=categoria_id)
    except Categoria.DoesNotExist:
        return JsonResponse({'error': 'Categoria não encontrada'}, status=404)

    categoria.delete()
    return JsonResponse({'message': 'Categoria excluída com sucesso!'}, status=200)

@api_view(['GET'])
def get_categoria(request, categoria_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Usuário não autenticado'}, status=403)

    try:
        categoria = Categoria.objects.get(id=categoria_id)
    except Categoria.DoesNotExist:
        return JsonResponse({'error': 'Categoria não encontrada'}, status=404)

    return JsonResponse({
        'id': categoria.categoria_id,
        'nome': categoria.nome,
        'descricao_categoria': categoria.descricao_categoria,
        'localizacao': categoria.localizacao
    })


@api_view(['GET'])
def search(request):
    query = request.GET.get('query', '')
    data = {
        'Produtos': list(Produto.objects.filter(nome_produto__icontains=query).values()),
        'Categorias': list(Categoria.objects.filter(descricao_categoria__icontains=query).values()),
        'Fornecedores': list(Fornecedor.objects.filter(nome_fantasia__icontains=query).values()),
        'Funcionários': list(CustomUser.objects.filter(primeiro_nome__icontains=query).values()),
    }
    return JsonResponse(data, safe=False)
