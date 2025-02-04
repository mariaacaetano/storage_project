# serializers.py
from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id_produto', 'nome_produto', 'preco_produto', 'quantidade', 'codigo_produto', 'status', 'categoria','fornecedor',]  # Adicione outros campos que você quer retornar

    def validate_nome(self, value):
        if not value:
            raise serializers.ValidationError("Nome do produto não pode ser vazio.")
        return value