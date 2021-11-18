from django.urls import path
from web.views import *

urlpatterns = [
    #Categorias
    path('categorias_list/', CategoriaView.as_view(), name='categorias_list'),
    path('categoria_new/', CategoriaNew.as_view(), name='categoria_new'),
    path('categoria_edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categoria_delete/<int:pk>', CategoriaDel.as_view(), name='categoria_delete'),

    #SubCategorias
    path('subcategorias_list/', SubCategoriaView.as_view(), name='subcategorias_list'),
    path('subcategoria_new/', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategoria_edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategoria_delete/<int:pk>', SubCategoriaDel.as_view(), name='subcategoria_delete'),
    
    #Marcas
    path('marcas_list/', MarcaView.as_view(), name='marcas_list'),
    path('marca_new/', MarcaNew.as_view(), name='marca_new'),
    path('marca_edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
    path('marca_delete/<int:pk>', MarcaDel.as_view(), name='marca_delete'),
    
    #Productos
    path('productos_list/', ProductoView.as_view(), name='productos_list'),
    #path('producto_new/', MarcaNew.as_view(), name='producto_new'),
    #path('producto_edit/<int:pk>', MarcaEdit.as_view(), name='producto_edit'),
    #path('producto_delete/<int:pk>', MarcaDel.as_view(), name='producto_delete'),
]
