from django.urls import path
from . import views
urlpatterns = [
    path('',views.Herramientas_View,name='Herramientas_Views'),
    
    path('ingreso_herramienta/',views.form_Ingreso,name="ingreso_herramienta"),
    path('ingreso_acta/',views.form_Ingreso,name="ingreso_acta"),

    path('Editar_Herramienta/<int:id_articulo>',views.Editar,name="Editar_Herramienta"),
    path('Editar_Acta/<int:id_articulo>',views.Editar,name="Editar_Acta"),
    path('Editar_form_Herramienta/<int:id_articulo>',views.Editar_form,name="Editar_form_Herramienta"),
    path('Editar_form_acta/<int:id_articulo>',views.Editar_form,name="Editar_form_Acta"),

    path('confirmar_eliminacion_herramienta/<int:id_articulo>',views.confirmacion_eliminar,name="confirmar_herramienta"),
    path('confirmar_eliminacion/<int:id_articulo>',views.confirmacion_eliminar,name="confirmar_acta"),
    path('Eliminar_Herramienta/<int:id_articulo>',views.Eliminar,name="Eliminar_Herramienta"),
    path('Eliminar_Acta/<int:id_articulo>',views.Eliminar,name="Eliminar_Acta"),
    ]