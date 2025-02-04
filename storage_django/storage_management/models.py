from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=500, verbose_name="Razão Social")
    nome_fantasia = models.CharField(max_length=500, verbose_name="Nome Fantasia")
    cnpj = models.CharField(max_length=15, verbose_name="CNPJ")
    inscricao_estadual = models.CharField(max_length=9, verbose_name="Inscrição Estadual")
    telefone = models.IntegerField(verbose_name="Telefone")
    endereco = models.CharField(max_length=500, verbose_name="Endereço")
    tipo_produto = models.CharField(max_length=500, verbose_name="Tipo de Produto")
    
    def __str__(self):
        return self.nome_fantasia
    
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, default='', verbose_name='Nome da Categoria')
    descricao_categoria = models.CharField(max_length=500, verbose_name="Descrição da Categoria")
    localizacao = models.CharField(max_length=500, verbose_name="Localização")
    
    def __str__(self):
        return self.descricao_categoria
    

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=500, verbose_name="Nome do Produto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    codigo_produto = models.CharField(max_length=13, verbose_name="Código do Produto")
    preco_produto = models.FloatField(verbose_name="Preço do Produto")
    status = models.BooleanField(default=True, verbose_name="Status")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome_produto
    
