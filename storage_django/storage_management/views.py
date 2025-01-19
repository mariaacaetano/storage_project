from django.http import JsonResponse
from .models import Produto, Categoria, Fornecedor
from customuser.models import CustomUser


class BaseSiteViews(View):
    data_table = None 

    def get(self, request):
        objects = self.data_table.objects.all()
        return JsonResponse(list(objects.values()), safe=False)

    def post(self, request):
        data = request.POST
        instance = self.data_table.objects.create(**data)
        return JsonResponse({'id': instance.pk, 'message': 'Created successfully'}, status=201)

    def delete(self, request):
        obj_id = request.POST.get('id')
        self.data_table.objects.filter(id=obj_id).delete()
        return JsonResponse({'message': 'Deleted successfully'}, status=200)

    def put(self, request):
        obj_id = request.POST.get('id')
        data = request.POST
        obj = self.data_table.objects.filter(id=obj_id).update(**data)
        return JsonResponse({'message': 'Updated successfully'}, status=200)

    def read(self, request):
        obj_id = request.GET.get('id')
        obj = self.data_table.objects.filter(id=obj_id).values()
        if not obj:
            return JsonResponse({'error': 'Not found'}, status=404)
        return JsonResponse(list(obj)[0], safe=False)


class ProductsView(BaseSiteViews):
    data_table = Produto


class CategoriesView(BaseSiteViews):
    data_table = Categoria


class SupplierView(BaseSiteViews):
    data_table = Fornecedor


class SearchView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        data = {
            'Produtos': list(Produto.objects.filter(nome_produto__icontains=query).values()),
            'Categorias': list(Categoria.objects.filter(descricao_categoria__icontains=query).values()),
            'Fornecedores': list(Fornecedor.objects.filter(nome_fantasia__icontains=query).values()),
            'Funcionários': list(CustomUser.objects.filter(primeiro_nome__icontains=query).values()),
        }
        return JsonResponse(data, safe=False)
