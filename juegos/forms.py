from django import forms
from .models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.Select,
        empty_label="Seleccione una categoría"
    )
    class Meta:
        model = Producto
        fields = ['nombre', 'url_imagen', 'descripcion', 'precio', 'categoria']
