from django.db import models
from base.models import ClaseModelo



class Categoria(ClaseModelo):
    descripcion = models.CharField('Descripción', max_length=100, help_text='Descripción de la categoría')

    def __str__(self):
        return self.descripcion

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = 'Categorías'

class SubCategoria(ClaseModelo):
    descripcion = models.CharField('Descripción', max_length=100, help_text='Descripción de la subcategoría')

    def __str__(self):
        return self.descripcion

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = 'SubCategorías'

class Marca(ClaseModelo):
    descripcion = models.CharField('Descripción', max_length=100, help_text='Descripción de la marca')

    def __str__(self):
        return self.descripcion

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = 'Marcas'

class Producto(ClaseModelo):
    descripcion = models.CharField('Descripcion', max_length=100, help_text='Descripción del producto')
    stock = models.IntegerField('Stock', default=0)
    preciodistrib = models.IntegerField('Distribuidor', default=0)
    precioferret = models.IntegerField('Ferreteria', default=0)
    preciopubl = models.IntegerField('Publico', default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    estado = models.BooleanField('Estado', default=True)