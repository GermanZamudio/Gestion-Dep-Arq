from django.shortcuts import render
from .models import (
    ArticuloUsoDiario,
    ArticuloLicitacion,
    MovimientoUsoDiario,
    MovimientoLicitacion,
)
from .form import FormArticuloLicitacion, FormArticulo, FormMovimiento,FormMovimientoLicitacion
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.urls import resolve
# Create your views here.

def InventaryView(request):
    # Accedemos al input de busqueda y evaluamos si el usuario inicio una busqueda.
    busqueda = request.GET.get("Buscar", "")
    mayor_o_menor=5
    if busqueda:
        Articulos = ArticuloUsoDiario.objects.filter(
            Q(codigo__icontains=busqueda)
            | Q(nombre__icontains=busqueda)
            | Q(marca__icontains=busqueda)
            | Q(IdUbicacion__ubicacion__icontains=busqueda)
            | Q(Descripcion__icontains=busqueda)
            | Q(IdCategorias__Nombre__icontains=busqueda)
            | Q(Existencias__icontains=busqueda)
            | Q(utilidad__Accion__icontains=busqueda)
        ).distinct()
        Articulos_Licitacion = ArticuloLicitacion.objects.filter(
            Q(codigo__icontains=busqueda)
            | Q(nombre__icontains=busqueda)
            | Q(marca__icontains=busqueda)
            | Q(IdUbicacion__ubicacion__icontains=busqueda)
            | Q(IdCategorias__Nombre__icontains=busqueda)
            | Q(Existencias__icontains=busqueda)
            | Q(licitacion__codigo_folio__icontains=busqueda)
        )
        mayor_o_menor=10
    else:
        # Caso contrario pasamos al contexto todos los articulos de la base de datos.
        Articulos = ArticuloUsoDiario.objects.all().order_by("utilidad")
        Articulos_Licitacion = ArticuloLicitacion.objects.all().order_by("-IdUbicacion")
    return render(
        request,"Inventario/Inventario.html",{
            "Articulos": Articulos,
            "Articulos_Licitacion": Articulos_Licitacion,
            "usuario": request.user.username,
            "mayor_o_menor":mayor_o_menor,
        },
    )

@login_required
def Ingresar_form(request):
    if request.method == "GET":
        resolved_url = resolve(request.path_info).url_name
        if resolved_url == 'Ingreso_licitacion':
            form = FormArticuloLicitacion()
            return render(request, "Inventario/Articulos_diarios/FormArticulos.html", {"form": form, "Licitacion": "Licitacion"})
        elif resolved_url == "Ingreso":
            form = FormArticulo()
            return render(request, "Inventario/Articulos_diarios/FormArticulos.html", {"form": form, "Diario": "Diario"})
    else:
        resolved_url = resolve(request.path_info).url_name
        if resolved_url == 'Ingreso_licitacion':
            form_Ingreso = FormArticuloLicitacion(request.POST)
        elif resolved_url == 'Ingreso':
            form_Ingreso = FormArticulo(request.POST)

        if form_Ingreso.is_valid():
            form_Ingreso.save()
            if resolved_url == 'Ingreso_licitacion':
                Articulo = ArticuloLicitacion.objects.last()
                fecha_actual = datetime.now()
                fecha_formateada = fecha_actual.strftime("%Y-%m-%d")
                Registro = MovimientoLicitacion(
                    fecha=fecha_formateada,
                    accion="Ingreso articulo licitacion",
                    articulo_licitacion=Articulo.nombre,
                    Cantidad=Articulo.Existencias,
                    Licitacion=Articulo.licitacion,
                    marca=Articulo.marca,
                    Destino="",
                    Ubicacion=Articulo.IdUbicacion.ubicacion,
                    Numero_de_Orden="Cambiar",
                    Entrega_conforme="",
                    Recibe_conforme=request.user.username,
                )
                Registro.save()
            elif resolved_url == 'Ingreso':
                Articulo = ArticuloUsoDiario.objects.last()
                fecha_actual = datetime.now()
                fecha_formateada = fecha_actual.strftime("%Y-%m-%d")

                Registro = MovimientoUsoDiario(
                    fecha=fecha_formateada,
                    accion="Ingreso articulo uso diario",
                    Nombre_de_Articulo=Articulo.nombre,
                    Cantidad=Articulo.Existencias,
                    marca=Articulo.marca,
                    Codigo=Articulo.codigo,
                    Destino="",
                    Ubicacion=Articulo.IdUbicacion.ubicacion,
                    Entrega_conforme="",
                    Recibe_conforme=request.user.username,
                )
                Registro.save()

            if 'guardar_y_agregar_otro' in request.POST:
                if resolved_url == 'Ingreso_licitacion':
                    form = FormArticuloLicitacion()
                    return render(request, "Inventario/Articulos_diarios/FormArticulos.html", {"form": form, "Licitacion": "Licitacion"})
                elif resolved_url == 'Ingreso':
                    form = FormArticulo()
                    return render(request, "Inventario/Articulos_diarios/FormArticulos.html", {"form": form, "Diario": "Diario"})

        else:
            return render(
                request, "Inventario/Articulos_diarios/FormArticulos.html",
                {"form": form_Ingreso, "Licitacion": "Licitacion" if resolved_url == 'Ingreso_licitacion' else "Diario", "error": "error"}
            )

        Articulos = ArticuloUsoDiario.objects.all().order_by("utilidad")
        Articulos_Licitacion = ArticuloLicitacion.objects.all().order_by("-IdUbicacion")
        return render(
            request,
            "Inventario/Inventario.html",
            {
                "Articulos": Articulos,
                "Articulos_Licitacion": Articulos_Licitacion,
                "usuario": request.user.username,
            },
        )

@login_required
def Editar(request, id_articulo):
    resolved_url = resolve(request.path_info).url_name
    if resolved_url=='Editar_Articulo':
        # Primero traemos el articulo atraves del id que selecciono el usuario.
        articulo_update = ArticuloUsoDiario.objects.filter(id=id_articulo).first()
        # Cargamos ese articulo en el form y lo pasamos al template para que el usuario lo modifique
        form_articulo = FormArticulo(instance=articulo_update)
        form_movimiento = FormMovimiento()
        # cargamos al formulario de movimientos los datos que deben mantenerse igual, ya que no figuran en el template
        form_movimiento.fields["Nombre_de_Articulo"].initial = articulo_update.nombre
        form_movimiento.fields["Codigo"].initial = articulo_update.codigo
        form_movimiento.fields["Ubicacion"].initial = articulo_update.IdUbicacion
        return render(
            request,
            "Inventario/Articulos_diarios/Editar.html",
            {
                "form": form_articulo,
                "form_mov": form_movimiento,
                "Articulo": articulo_update,
                "Diario":"Diario",
            },
        )
    else:
        # Primero traemos el articulo atraves del id que selecciono el usuario.
        articulo_lic_update = ArticuloLicitacion.objects.filter(id=id_articulo).first()
        # Cargamos ese articulo en el form y lo pasamos al template para que el usuario lo modifique
        form_articulo_lic = FormArticuloLicitacion(instance=articulo_lic_update)
        form_movimiento_lic = FormMovimientoLicitacion()
        # cargamos al formulario de movimientos los datos que deben mantenerse igual, ya que no figuran en el template
        form_movimiento_lic.fields["articulo_licitacion"].initial = articulo_lic_update.nombre
        form_movimiento_lic.fields["Licitacion"].initial = articulo_lic_update.licitacion
        form_movimiento_lic.fields["Ubicacion"].initial = articulo_lic_update.IdUbicacion

        return render(
            request,
            "Inventario/Articulos_diarios/Editar.html",
            {
                "form": form_articulo_lic,
                "form_mov": form_movimiento_lic,
                "Articulo": articulo_lic_update,
                "Licitacion":"Licitacion",
            },
        )
    
@login_required
def Editar_form(request, id_articulo):
    resolved_url = resolve(request.path_info).url_name
    if resolved_url=='Editar_form':
        articulo_update = ArticuloUsoDiario.objects.get(pk=id_articulo)
        form_articulo = FormArticulo(request.POST, instance=articulo_update)
        form_movimiento = FormMovimiento(request.POST)
        # Si son validos se guardan.
        if form_articulo.is_valid() and form_movimiento.is_valid():
            form_articulo.save()
            form_movimiento.save()

            # Aca tuve que hacer un guardado posterior, porque en caso que
            # Modifique el nombre o el codigo, queda guardado el anterior
            # Entonces tengo que modificar el registro luego de que
            # ya haya guardado el formulario.

            Articulo_actualizado = ArticuloUsoDiario.objects.get(pk=id_articulo)
            ultima_modificacion = MovimientoUsoDiario.objects.latest("id")
            ultima_modificacion.Nombre_de_Articulo = Articulo_actualizado.nombre
            ultima_modificacion.Codigo = Articulo_actualizado.codigo
            #ultima_modificacion.Ubicacion=Articulo_actualizado.IdUbicacion.ubicacion
            modificacion_existencias=ArticuloUsoDiario.objects.get(pk=id_articulo)
            modificacion_existencias.Existencias=modificacion_existencias.Existencias-ultima_modificacion.Cantidad
            modificacion_existencias.save()
            ultima_modificacion.save()

            if modificacion_existencias.Existencias<0:
                modificacion_existencias.delete()
            # Le pasamos todos los articulos a la vista inventario
            Articulos = ArticuloUsoDiario.objects.all().order_by("utilidad")
            Articulos_Licitacion = ArticuloLicitacion.objects.all().order_by("-IdUbicacion")
            return render(
                request,
                "Inventario/Inventario.html",
                {
                    "Articulos": Articulos,
                    "Articulos_Licitacion": Articulos_Licitacion,
                    "usuario": request.user.username,
                },
            )
        else:
            return render(
                request,
                "Inventario/Articulos_diarios/Editar.html",
                {
                    "form": form_articulo,
                    "form_mov": form_movimiento,
                    "error": "error",
                    "Articulo": articulo_update,
                    "Diario":"Diario",
                },
            )
    elif resolved_url=='Editar_form_Licitacion':
        articulo_update = ArticuloLicitacion.objects.get(pk=id_articulo)
        form_articulo_lic = FormArticuloLicitacion(request.POST, instance=articulo_update)
        form_movimiento_lic = FormMovimientoLicitacion(request.POST)
        # Si son validos se guardan.
        if form_articulo_lic.is_valid() and form_movimiento_lic.is_valid():
            form_articulo_lic.save()
            form_movimiento_lic.save()
            # Aca tuve que hacer un guardado posterior, porque en caso que
            # Modifique el nombre o el codigo, queda guardado el anterior
            # Entonces tengo que modificar el registro luego de que
            # ya haya guardado el formulario.

            Articulo_actualizado = ArticuloLicitacion.objects.get(pk=id_articulo)
            ultima_modificacion = MovimientoLicitacion.objects.latest("id")
            ultima_modificacion.articulo_licitacion = Articulo_actualizado.nombre
            ultima_modificacion.Licitacion = Articulo_actualizado.licitacion.codigo_folio
            #ultima_modificacion.Ubicacion=Articulo_actualizado.IdUbicacion
            ultima_modificacion.save()

            # Le pasamos todos los articulos a la vista inventario
            Articulos = ArticuloUsoDiario.objects.all().order_by("utilidad")
            Articulos_Licitacion = ArticuloLicitacion.objects.all().order_by("-IdUbicacion")
            return render(
                request,
                "Inventario/Inventario.html",
                {
                    "Articulos": Articulos,
                    "Articulos_Licitacion": Articulos_Licitacion,
                    "usuario": request.user.username,
                },
            )
        else:
            return render(
                request,
                "Inventario/Articulos_diarios/Editar.html",
                {
                    "form": form_articulo_lic,
                    "form_mov": form_movimiento_lic,
                    "error": "error",
                    "Articulo": articulo_update,
                    "Licitacion":"Licitacion",
                },
            )
    else:
        # Caso contrario pasamos al contexto todos los articulos de la base de datos.
        Articulos = ArticuloUsoDiario.objects.all().order_by("utilidad")
        Articulos_Licitacion = ArticuloLicitacion.objects.all().order_by("-IdUbicacion")
        return render(
            request,"Inventario/Inventario.html",{
                "Articulos": Articulos,
                "Articulos_Licitacion": Articulos_Licitacion,
                "usuario": request.user.username,
            },
        )

@login_required
def confirmacion_eliminar(request,id_articulo):
    resolved_url = resolve(request.path_info).url_name
    if resolved_url=='confirmar_articulo':
        return render(request, "Inventario/Articulos_diarios/confirmar.html", {"id": id_articulo,"Diario":"Diario"})
    else:
        return render(request, "Inventario/Articulos_diarios/confirmar.html", {"id": id_articulo,"Licitacion":"Licitacion"})
    


@login_required
def Eliminar_Articulo(request, id_articulo):
    
    resolved_url = resolve(request.path_info).url_name
    if resolved_url=='Eliminar_Articulo':
        articulo_delete = ArticuloUsoDiario.objects.get(pk=id_articulo)
        #Registramos la eliminacion en movimientos:
        fecha_actual = datetime.now()
        Registro_de_eliminacion = MovimientoUsoDiario(
                    fecha=fecha_actual.strftime("%Y-%m-%d"),
                    accion="Eliminacion",
                    Nombre_de_Articulo=articulo_delete.nombre,
                    Cantidad=0,
                    Codigo=0,
                    Destino="",
                    Ubicacion=articulo_delete.IdUbicacion,
                    Entrega_conforme="",
                    Recibe_conforme=request.user.username,
                )
        Registro_de_eliminacion.save()
        #Guardamos la eliminacion en la base de datos
        articulo_delete.delete()
    elif resolved_url=="Eliminar_Articulo_Licitacion":
        articulo_delete= ArticuloLicitacion.objects.get(pk=id_articulo)
        #Registramos la eliminacion en movimientos:
        fecha_actual = datetime.now()
        Registro_de_eliminacion = MovimientoLicitacion(
                    fecha=fecha_actual.strftime("%Y-%m-%d"),
                    accion="Eliminacion",
                    articulo_licitacion=articulo_delete.nombre,
                    Cantidad=0,
                    Licitacion=articulo_delete.licitacion,
                    marca=articulo_delete.marca,
                    Destino="",
                    Ubicacion=articulo_delete.IdUbicacion,
                    Entrega_conforme="",
                    Recibe_conforme=request.user.username,
                )
        Registro_de_eliminacion.save()
        #Guardamos la eliminacion en la base de datos
        articulo_delete.delete()
    # Le pasamos todos los articulos a la vista inventario
    Articulos = ArticuloUsoDiario.objects.all().order_by("utilidad")
    Articulos_Licitacion = ArticuloLicitacion.objects.all().order_by("-IdUbicacion")
    return render(
            request,
            "Inventario/Inventario.html",
            {
                "Articulos": Articulos,
                "Articulos_Licitacion": Articulos_Licitacion,
                "usuario": request.user.username,
            },
        )

    
    #Movimientos:
@login_required
def Registro_Movimientos(request):
    busqueda = request.GET.get("Buscar", "")
    mayor_o_menor=5
    if busqueda:
            Movimientos_diarios = MovimientoUsoDiario.objects.filter(
                Q(fecha__icontains=busqueda)
                | Q(accion__icontains=busqueda)
                | Q(Nombre_de_Articulo__icontains=busqueda)
                | Q(Codigo__icontains=busqueda)
                | Q(Entrega_conforme__icontains=busqueda)
                | Q(Recibe_conforme__icontains=busqueda)
            ).distinct()
            Movimientos_Licitacion = MovimientoLicitacion.objects.filter(
                Q(fecha__icontains=busqueda)
                | Q(accion__icontains=busqueda)
                | Q(articulo_licitacion__icontains=busqueda)
                | Q(Licitacion__icontains=busqueda)
                | Q(Entrega_conforme__icontains=busqueda)
                | Q(Recibe_conforme__icontains=busqueda)
            )
            mayor_o_menor=10
    else:
            # Caso contrario pasamos al contexto todos los articulos de la base de datos.
            Movimientos_diarios = MovimientoUsoDiario.objects.all().order_by("-fecha")
            Movimientos_Licitacion = MovimientoLicitacion.objects.all().order_by("-fecha")
    return render(
            request,
            "Inventario/Movimientos/Movimientos.html",
            {
                "Articulos": Movimientos_diarios,
                "Articulos_Licitacion": Movimientos_Licitacion,
                "usuario": request.user.username,
                "mayor_o_menor":mayor_o_menor,
            },
        )

@login_required
def Agregar_Orden(request,id_articulo):
    
    if request.method == "GET":
        
        Acta =MovimientoLicitacion.objects.filter(id=id_articulo).first()
        form=FormMovimientoLicitacion(instance=Acta)
        return render(
            request,
            "Inventario/Movimientos/Agregar_Orden.html",
            {
                "form": form,
                "Acta":Acta,
                "Agregar":"Agregar",
            },
        )
    else:
        Num_update = MovimientoLicitacion.objects.get(pk=id_articulo)
        form = FormMovimientoLicitacion(request.POST, instance=Num_update)
        if form.is_valid():
            form.save()
        
        Movimientos_diarios = MovimientoUsoDiario.objects.all().order_by("-fecha")
        Movimientos_Licitacion = MovimientoLicitacion.objects.all().order_by("-fecha")
        mayor_o_menor=5    
        return render(
                    request,
                    "Inventario/Movimientos/Movimientos.html",
                    {
                        "Articulos": Movimientos_diarios,
                        "Articulos_Licitacion": Movimientos_Licitacion,
                        "usuario": request.user.username,
                        "mayor_o_menor":mayor_o_menor,
                    },
                )

@login_required
def confirmacion_registro(request,id_articulo):
        resolved_url = resolve(request.path_info).url_name
        if resolved_url=='confirmar_registro':
            return render(request, "Inventario/Movimientos/confirmar_registro.html", {"id": id_articulo,"Diario":"Diario"})
        else:
            return render(request, "Inventario/Movimientos/confirmar_registro.html", {"id": id_articulo,"Licitacion":"Licitacion"})
        


@login_required
def Eliminar_Registro(request, id_articulo):
        
        resolved_url = resolve(request.path_info).url_name
        if resolved_url=='Eliminar_Registro':
            articulo_delete = MovimientoUsoDiario.objects.get(pk=id_articulo)
            articulo_delete.delete()
        else:
            articulo_delete= MovimientoLicitacion.objects.get(pk=id_articulo)
            articulo_delete.delete()
        Movimientos_diarios = MovimientoUsoDiario.objects.all().order_by("-fecha")
        Movimientos_Licitacion = MovimientoLicitacion.objects.all().order_by("-fecha")
        
        mayor_o_menor=5
        return render(
            request,
            "Inventario/Movimientos/Movimientos.html",
            {
                "Articulos": Movimientos_diarios,
                "Articulos_Licitacion": Movimientos_Licitacion,
                "usuario": request.user.username,
                "mayor_o_menor":mayor_o_menor,
            },
        )

