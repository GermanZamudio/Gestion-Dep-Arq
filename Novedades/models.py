from django.db import models

# Create your models here.

class Novedad(models.Model):
    fecha= models.DateTimeField(auto_now_add=True)
    usuario=models.CharField(max_length=30)
    Texto=models.TextField()
