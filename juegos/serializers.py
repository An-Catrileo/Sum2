from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'genero', 'descripcion', 'precio']#campos a incluir en la Api
        
        

        
        
        