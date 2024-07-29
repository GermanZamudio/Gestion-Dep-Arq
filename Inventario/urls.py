
from django.urls import path
from . import views
urlpatterns = [
    path('',views.InventaryView,name='Inventario'),
    #Articulos de uso diario:
    path('Ingreso/',views.Ingresar_form,name="Ingreso"),
    path('Editar_Articulo/<int:id_articulo>',views.Editar,name="Editar_Articulo"),
    path('Editar_form/<int:id_articulo>',views.Editar_form,name="Editar_form"),
    path('Eliminar_Articulo/<int:id_articulo>',views.Eliminar_Articulo,name="Eliminar_Articulo"),
    path('confirmar_articulo/<int:id_articulo>',views.confirmacion_eliminar,name="confirmar_articulo"),
    #Articulos de licitacion: 
    path('Ingreso_licitacion/',views.Ingresar_form,name="Ingreso_licitacion"),
    path('Editar_Articulo_Licitacion/<int:id_articulo>',views.Editar,name="Editar_Articulo_Licitacion"),
    path('Editar_form_Licitacion/<int:id_articulo>',views.Editar_form,name="Editar_form_Licitacion"),
    path('confirmar_licitacion/<int:id_articulo>',views.confirmacion_eliminar,name="confirmar_licitacion"),
    path('Eliminar_Articulo_Licitacion/<int:id_articulo>',views.Eliminar_Articulo,name="Eliminar_Articulo_Licitacion"),
    #Registro Movimientos:
    path('Movimientos/',views.Registro_Movimientos,name="Movimientos"),
    path('Agregar_Num_Orden/<int:id_articulo>',views.Agregar_Orden,name="Agregar_Num_Orden"),
    
    path('confirmar_registro/<int:id_articulo>',views.confirmacion_registro,name="confirmar_registro"),
    path('Eliminar_Registro/<int:id_articulo>',views.Eliminar_Registro,name="Eliminar_Registro"),

    path('confirmar_registro_licitacion/<int:id_articulo>',views.confirmacion_registro,name="confirmar_registro_licitacion"),
    path('Eliminar_Registro_Licitacion/<int:id_articulo>',views.Eliminar_Registro,name="Eliminar_Registro_Licitacion"),
    
]
