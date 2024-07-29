
from django.contrib import admin
from .models import Herramientas,Acta_entrega_herramienta,Prestamo

class Prestamos(admin.TabularInline):
    model=Prestamo
    extra=1

class ActaAdmin(admin.ModelAdmin):
    inlines=[Prestamos]
"""    list_display=('nombre','cantidad','marca','ubicacion','Funcion')
    def full_name(self,obj):
        return obj.nombre + ' ' + obj.cantidad
    search_fields=('nombre')
    list_filter=('ubicacion')
    filter_horizontal=['ubicacion']
"""
admin.site.register(Herramientas)

admin.site.register(Prestamo)
admin.site.register(Acta_entrega_herramienta, ActaAdmin)

