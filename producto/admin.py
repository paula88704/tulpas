from django.contrib import admin

from .models import producto, tipo, mesa, cliente, proveedor, empleados

@admin.register(tipo)
class tipo(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

@admin.register(producto)

class producto(admin.ModelAdmin):
    list_display = ('tipo', 'nombre', 'descripcion','precio','activo','fecha_creado', 'fecha_vencimiento')

@admin.register(mesa)
class mesa(admin.ModelAdmin):
    list_display = ('numero_mesa', 'capacidad', 'estado','fecha_creado')

@admin.register(cliente)
class cliente(admin.ModelAdmin):
    list_display = ('nombre', 'direccion','telefono','email')

@admin.register(proveedor)
class proveedor(admin.ModelAdmin):
    list_display = ('nombre', 'direccion','telefono','email','activo')

@admin.register(empleados)
class empelados(admin.ModelAdmin):
    list_display = ('nombre', 'cargo','telefono')