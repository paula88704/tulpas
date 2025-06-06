from rest_framework import serializers
from .models import tipo, producto, mesa, cliente, proveedor, empleados

class TipoSerializer(serializers.ModelSerializer):  
    class Meta:
        model = tipo
        fields = '__all__'
        read_only_fields = ('fecha_creado',)

class ProductoSerializer(serializers.ModelSerializer):  
    class Meta:
        model = producto
        fields = '__all__'
        read_only_fields = ('fecha_creado',)
 
    
class MesaSerializer(serializers.ModelSerializer):  
    class Meta:
        model = mesa
        fields = '__all__'
        read_only_fields = ('fecha_creado',)


class ClienteSerializer(serializers.ModelSerializer):  
    class Meta:
        model = cliente
        fields = '__all__'
        read_only_fields = ('fecha_creado',)


class ProveedorSerializer(serializers.ModelSerializer):  
    class Meta:
        model = proveedor
        fields = '__all__'
        read_only_fields = ('fecha_creado',)

class EmpleadosSerializer(serializers.ModelSerializer):  
    class Meta:
        model = empleados
        fields = '__all__'
        read_only_fields = ('fecha_creado',)