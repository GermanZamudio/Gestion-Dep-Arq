
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Novedad_View,name='Novedad'),
    path('Eliminar_Novedad/<int:Novedad_id>',views.Eliminar_Novedad,name="Eliminar_Novedad"),
]
