from django.urls import path
from .views import ProductsView, CategoriesView, SupplierView, SearchView

urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('suppliers/', SupplierView.as_view(), name='suppliers'),
    path('search/', SearchView.as_view(), name='search'),
]
