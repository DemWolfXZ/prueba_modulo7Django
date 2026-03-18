from django.db import models


# Create your models here.

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre_cliente
    
    
class GeneroJuego(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_genero


class Plataforma(models.Model):
    id_plataforma = models.AutoField(primary_key=True)
    nombre_plataforma = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_plataforma
    
    
class Juego(models.Model):
    id_juego = models.AutoField(primary_key=True)
    nombre_juego = models.CharField(max_length=100)
    genero = models.ForeignKey('GeneroJuego', on_delete=models.CASCADE)
    plataforma = models.ForeignKey('Plataforma', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    # NUEVO
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='juegos/', blank=True, null=True)

    def __str__(self):
        return self.nombre_juego
    
    
class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    total_boleta = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Boleta {self.id_boleta} - Cliente: {self.cliente.nombre_cliente}"


class DetalleBoleta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.id_detalle} - {self.juego.nombre_juego}"