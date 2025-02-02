from django.urls import path
from . import views

urlpatterns = [
    # URLs para os Produtos
    path('produtos/', views.list_produtos, name='list_produtos'),
    path('produtos/<int:produto_id>/', views.get_produto, name='get_produto'),
    path('produtos/<int:produto_id>/update/', views.update_produto, name='update_produto'),
    path('produtos/<int:produto_id>/delete/', views.delete_produto, name='delete_produto'),
    
    # URLs para criação de Produtos
    path('create_produto/', views.create_produto, name='create_produto'),

    # URLs para as Categorias
    path('categorias/', views.list_categorias, name='list_categorias'),
    path('categorias/<int:categoria_id>/', views.get_categoria, name='get_categoria'),
    path('categorias/<int:categoria_id>/update/', views.update_categoria, name='update_categoria'),
    path('categorias/<int:categoria_id>/delete/', views.delete_categoria, name='delete_categoria'),
    path('categorias/detail/<int:id>/', views.categoria_detail, name='categoria_detail'),  # Ajustei o path para a URL de detail de Categoria

    # URLs para criação de Categorias
    path('create_categoria/', views.create_categoria, name='create_categoria'),

    # URLs para os Fornecedores
    path('fornecedores/', views.list_fornecedores, name='list_fornecedores'),
    path('fornecedores/<int:fornecedor_id>/', views.get_fornecedor, name='get_fornecedor'),
    path('fornecedores/<int:fornecedor_id>/update/', views.update_fornecedor, name='update_fornecedor'),
    path('fornecedores/<int:fornecedor_id>/delete/', views.delete_fornecedor, name='delete_fornecedor'),
    
    # URLs para criação de Fornecedores
    path('create_fornecedor/', views.create_fornecedor, name='create_fornecedor'),

    # URL para a busca
    path('search/', views.search, name='search'),
]
