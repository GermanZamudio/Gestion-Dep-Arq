from django.db import models


class Licitacion(models.Model):
    codigo_folio = models.CharField(primary_key=True, max_length=100)
    def __str__(self):
        return self.codigo_folio

class Ubicacion(models.Model):
    ubicacion = models.CharField(max_length=30)

    def __str__(self):
        return self.ubicacion

class Categorias(models.Model):
    Nombre=models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

class Utilidad (models.Model):
    Accion= models.CharField(max_length=20)
    def __str__(self):
        return self.Accion
    
class ArticuloLicitacion(models.Model):
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    marca=models.CharField(max_length=20)
    Existencias=models.IntegerField()
    IdCategorias=models.ForeignKey(Categorias, on_delete=models.CASCADE,null=True)
    IdUbicacion=models.ForeignKey("Ubicacion", on_delete=models.CASCADE,null=True)
    saldo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_total = models.DecimalField(max_digits=10, decimal_places=2)
    licitacion = models.ForeignKey(Licitacion, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class ArticuloUsoDiario(models.Model):
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    marca=models.CharField(max_length=20)
    Descripcion=models.CharField(max_length=50)
    Existencias = models.IntegerField()
    IdCategorias=models.ForeignKey(Categorias, on_delete=models.CASCADE,null=True)
    IdUbicacion=models.ForeignKey("Ubicacion", on_delete=models.CASCADE,null=True)
    utilidad = models.ForeignKey(Utilidad, on_delete=models.CASCADE,null=True)
    saldo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_total = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nombre



class MovimientoLicitacion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    accion = models.CharField(max_length=30)
    articulo_licitacion = models.CharField(max_length=30)
    marca=models.CharField(max_length=20)
    Licitacion=models.CharField(max_length=40)
    Cantidad=models.IntegerField()
    Destino = models.CharField(max_length=30)
    Numero_de_Orden=models.CharField(max_length=30)
    Ubicacion=models.CharField(max_length=30)
    Entrega_conforme = models.CharField(max_length=30)
    Recibe_conforme = models.CharField(max_length=30)



class MovimientoUsoDiario(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    Nombre_de_Articulo = models.CharField(max_length=30)
    marca=models.CharField(max_length=20)
    Codigo=models.CharField(max_length=30)
    Destino = models.CharField(max_length=30)
    accion = models.CharField(max_length=30)
    Cantidad=models.IntegerField()
    Ubicacion = models.CharField(max_length=30)
    Entrega_conforme = models.CharField(max_length=30)
    Recibe_conforme = models.CharField(max_length=30)
    
