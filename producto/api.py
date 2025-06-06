from producto.models import producto, tipo, mesa, cliente, proveedor, empleados
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializer, TipoSerializer, MesaSerializer, ClienteSerializer, ProveedorSerializer, EmpleadosSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset = tipo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoSerializer

class MesaViewSet(viewsets.ModelViewSet):
    queryset = mesa.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MesaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = proveedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer

class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = empleados.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadosSerializer