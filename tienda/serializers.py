
from .models import Categoria, Mascota
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class MascotaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only = True)
    Categoria_Id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source="categoria")
    nombreProducto = serializers.CharField(required = True, min_length=6)
    
    def valida_id (self, value):
        existe = Mascota.objects.filter(idProductomascota=value).exists()
        if existe:
            raise serializers.ValidationError("Este id ya existe")
        return value
    
    class Meta:
        model = Mascota
        fields = '__all__'
    