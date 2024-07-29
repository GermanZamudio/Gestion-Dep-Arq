
from django.contrib import admin
from .models import Categorias,Ubicacion,MovimientoUsoDiario,Licitacion,Utilidad
# Register your models here.


admin.site.register(Categorias)
admin.site.register(Ubicacion)
admin.site.register(MovimientoUsoDiario)
admin.site.register(Licitacion)
admin.site.register(Utilidad)