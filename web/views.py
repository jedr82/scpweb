from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from web.forms import CategoriaForm, MarcaForm, SubCategoriaForm
from web.models import Categoria, Marca, SubCategoria


class CategoriaView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'web/categorias_list.html'
    context_object_name = 'categoria'
    login_url = 'base:login'

class CategoriaNew(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'web/categoria_form.html'
    context_object_name = 'categoria'
    form_class = CategoriaForm
    success_url = reverse_lazy('web:categorias_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = 'web/categoria_form.html'
    context_object_name = 'categoria'
    form_class = CategoriaForm
    success_url = reverse_lazy('web:categorias_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class CategoriaDel(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'web/categoria_delete.html'
    context_object_name = 'categoria'
    success_url = reverse_lazy('web:categoria_list')

class SubCategoriaView(LoginRequiredMixin, ListView):
    model = SubCategoria
    template_name = 'web/subcategorias_list.html'
    context_object_name = 'subcategoria'
    login_url = 'base:login'

class SubCategoriaNew(LoginRequiredMixin, CreateView):
    model = SubCategoria
    template_name = 'web/subcategoria_form.html'
    context_object_name = 'subcategoria'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('web:subcategorias_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, UpdateView):
    model = SubCategoria
    template_name = 'web/subcategoria_form.html'
    context_object_name = 'subcategoria'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('web:subcategorias_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDel(LoginRequiredMixin, DeleteView):
    model = SubCategoria
    template_name = 'web/subcategoria_delete.html'
    context_object_name = 'subcategoria'
    success_url = reverse_lazy('web:subcategorias_list')
    
class MarcaView(LoginRequiredMixin, ListView):
    model = Marca
    template_name = 'web/marcas_list.html'
    context_object_name = 'marca'
    login_url = 'base:login'

class MarcaNew(LoginRequiredMixin, CreateView):
    model = Marca
    template_name = 'web/marca_form.html'
    context_object_name = 'marca'
    form_class = MarcaForm
    success_url = reverse_lazy('web:marcas_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, UpdateView):
    model = Marca
    template_name = 'web/marca_form.html'
    context_object_name = 'marca'
    form_class = MarcaForm
    success_url = reverse_lazy('web:marcas_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class MarcaDel(LoginRequiredMixin, DeleteView):
    model = Marca
    template_name = 'web/marca_delete.html'
    context_object_name = 'marca'
    success_url = reverse_lazy('web:marcas_list')