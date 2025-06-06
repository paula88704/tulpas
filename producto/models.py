from django.db import models 

class tipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)


    class Meta:
        ordering = ['-nombre']

    def __str__(self):
        return self.nombre
    
class producto(models.Model):
    tipo = models.ForeignKey(tipo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    activo = models.BooleanField(default=True)
    fecha_creado = models.DateTimeField(auto_now=True)
    fecha_vencimiento = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-nombre']

    def __str__(self):
        return self.nombre

class mesa(models.Model):
    numero_mesa = models.CharField(max_length=10, unique=True)
    capacidad = models.IntegerField(default=2)
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('ocupada', 'Ocupada'),
        ('reservada', 'Reservada'),
    ]
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='disponible',
    )
    fecha_creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['numero_mesa']
        verbose_name_plural = "Mesas"

    def _str_(self):
        return f"Mesa {self.numero_mesa} ({self.get_estado_display()})"


class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    fecha_creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-nombre']

    def _str_(self):
        return self.nombre_cliente

class proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['-nombre']

    def _str_(self):
        return self.nombre
    
class empleados(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    

    class Meta:
        ordering = ['-nombre']

    def _str_(self):
        return self.nombre
