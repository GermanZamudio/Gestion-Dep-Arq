from django.db import models
from Inventario.models import Ubicacion

class Herramientas(models.Model):
    nombre=models.CharField(max_length=25)
    marca=models.CharField(max_length=20)
    ubicacion=models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    Funcion=models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre
    
class Acta_entrega_herramienta(models.Model):
    fecha=models.DateField(auto_now_add=True)
    Destino=models.CharField(max_length=25)
    Herramienta=models.ManyToManyField(Herramientas, through='Prestamo' , blank=True,)
    Recibe=models.CharField(max_length=25)
    Entrega=models.CharField(max_length=25)
    def __str__(self):
        return self.Destino

    
class Prestamo(models.Model):
    herramienta= models.ForeignKey(Herramientas,on_delete=models.CASCADE,blank=True,null=True)
    acta=models.ForeignKey(Acta_entrega_herramienta,on_delete=models.CASCADE,blank=True,null=True)
    
    def __object__(self):
        return self.acta
    

