from django import forms
from web.models import Categoria, SubCategoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion':'Descripción de la categoría',
                  'estado':'Estado'}
        widget = {
            'descripcion': forms.TextInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class SubCategoriaForm(forms.ModelForm):
    class Meta:
        model = SubCategoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion':'Descripción de la subcategoría',
                  'estado':'Estado'}
        widget = {
            'descripcion': forms.TextInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })