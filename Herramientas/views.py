from django.shortcuts import render,redirect
from .models import Herramientas,Acta_entrega_herramienta,Prestamo
from .form import Form_Acta_trabajo,Form_Herramienta
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q
from django.urls import resolve
from Inventario.models import MovimientoUsoDiario
# Create your views here.

@login_required
def Herramientas_View(request):
    # Accedemos al input de busqueda y evaluamos si el usuario inicio una busqueda.
    busqueda = request.GET.get("Buscar", "")
    mayor_o_menor=5
    if busqueda:
        Herramienta= Herramientas.objects.filter(
            Q (nombre__icontains=busqueda)
            | Q(marca__icontains=busqueda)
            | Q(ubicacion__ubicacion__icontains=busqueda)
            | Q(Funcion__icontains=busqueda)
        ).distinct()
        mayor_o_menor=10
        Prestamos=Prestamo.objects.filter(
            Q(acta__fecha__icontains=busqueda)
            | Q(acta__Destino__icontains=busqueda)
            | Q(acta__Herramienta__nombre__icontains=busqueda)
            | Q(acta__Recibe__icontains=busqueda)
            | Q(acta__Entrega__icontains=busqueda)
        ).distinct()
    else:
        # Caso contrario pasamos al contexto todos los articulos de la base de datos.
        Herramienta = Herramientas.objects.all().order_by("nombre")
        Prestamos=Prestamo.objects.all().order_by("-acta")
    return render(
        request,"Herramientas/Views.html",{
            "Herramientas": Herramienta,'Prestamo':Prestamos,
            "usuario": request.user.username,
            "mayor_o_menor":mayor_o_menor,
        },
    )

@login_required
def form_Ingreso(request):
    if request.method == "GET":
        resolved_url = resolve(request.path_info).url_name
        if resolved_url=='ingreso_herramienta':
            # Pasamos al contexto el formulario de ingreso de articulos.
            form = Form_Herramienta()
            return render(request,
            "Herramientas/form.html",
            {"form": form,"herramienta":"herramienta"})
        elif resolved_url=="ingreso_acta":
            # Pasamos al contexto el formulario de ingreso de articulos.
            form = Form_Acta_trabajo()
            return render(request, 
            "Herramientas/form.html",
            {"form": form, "prestamo":"prestamo"})

    else:
        # Procesamos la informacion si es valida lo guardamos
        resolved_url = resolve(request.path_info).url_name
        if resolved_url=='ingreso_herramienta':
            form_Ingreso = Form_Herramienta(request.POST)
            if form_Ingreso.is_valid():
                form_Ingreso.save()
                if 'guardar_y_agregar_otro' in request.POST:
                    form = Form_Herramienta()
                    return render(request,
                        "Herramientas/form.html",
                        {"form": form,"herramienta":"herramienta"})
            else:
                return render(
                        request, "Herramientas/form.html", 
                        {"form": form_Ingreso, 
                        "error_Herramienta": "error_Herramienta"}
                    )
            
        # Procesamos la informacion si es valida lo guardamos
        elif resolved_url=='ingreso_acta':
            form_Ingreso = Form_Acta_trabajo(request.POST)
            if form_Ingreso.is_valid():
                form_Ingreso.save()
            else:
                return render(
                        request, "Herramientas/form.html", 
                        {"form": form_Ingreso, 
                        "error_Acta": "error_Acta"}
                    )
    # Le pasamos todos los articulos a la vista inventario
        Herramienta = Herramientas.objects.all().order_by("ubicacion")
        Acta_prestado=Acta_entrega_herramienta.objects.all().order_by("-fecha")
        Prestamos=Prestamo.objects.all().order_by("-acta")
        return render(
            request,"Herramientas/Views.html",{
                "Herramientas": Herramienta,'Prestamo':Prestamos,
                "usuario": request.user.username,
                "Acta":Acta_prestado,
            },
        )
            # Caso contrario pasamos al contexto todos los articulos de la base de datos.



@login_required
def Editar(request, id_articulo):
    resolved_url = resolve(request.path_info).url_name
    if resolved_url=='Editar_Herramienta':
        # Primero traemos el articulo atraves del id que selecciono el usuario.
        Herramienta_update = Herramientas.objects.filter(id=id_articulo).first()
        # Cargamos ese articulo en el form y lo pasamos al template para que el usuario lo modifique
        form_herramienta = Form_Herramienta(instance=Herramienta_update)
        return render(
            request,
            "Herramientas/Editar.html",
            {
                "form": form_herramienta,
                "Herramienta": Herramienta_update,
                "Edit_Herramienta":"Edit_Herramienta",
            },
        )
    else:
        # Primero traemos el articulo atraves del id que selecciono el usuario.
        acta_update = Acta_entrega_herramienta.objects.filter(id=id_articulo).first()
        # Cargamos ese articulo en el form y lo pasamos al template para que el usuario lo modifique
        form_acta= Form_Acta_trabajo(instance=acta_update)
        return render(
            request,
            "Herramientas/Editar.html",
            {
                "form": form_acta,
                "acta": acta_update,
                "Edit_acta":"Edit_acta",
            },
        )
    

@login_required
def Editar_form(request, id_articulo):
    resolved_url = resolve(request.path_info).url_name
    if resolved_url=='Editar_form_Herramienta':
        Herramienta = Herramientas.objects.get(pk=id_articulo)
        form_herramienta = Form_Herramienta(request.POST, instance=Herramienta)        
        # Si son validos se guardan.
        if form_herramienta.is_valid():
            form_herramienta.save()
            # Le pasamos todos los articulos a la vista inventario
            Herramienta = Herramientas.objects.all().order_by("ubicacion")
            Acta_prestado=Acta_entrega_herramienta.objects.all().order_by("-fecha")
            Prestamos=Prestamo.objects.all().order_by("-acta")
            return render(
                request,"Herramientas/Views.html",{
                    "Herramientas": Herramienta,'Prestamo':Prestamos,
                    "usuario": request.user.username,
                    "Acta":Acta_prestado,
                },
            )
        else:
            return render(
                request,
                "Herramientas/Editar.html",
                {
                    "form": form_herramienta,
                    "error": "error",
                    "Herramienta": Herramienta,
                    "Edit_Herramienta":"Edit_Herramienta",
                },
            )
    else:
        acta = Acta_entrega_herramienta.objects.get(pk=id_articulo)
        form_acta = Form_Acta_trabajo(request.POST, instance=acta)        
        # Si son validos se guardan.
        if form_acta.is_valid():
            form_acta.save()
            # Le pasamos todos los articulos a la vista inventario
            Herramienta = Herramientas.objects.all().order_by("ubicacion")
            Acta_prestado=Acta_entrega_herramienta.objects.all().order_by("-fecha")
            Prestamos=Prestamo.objects.all().order_by("-acta")
            return render(
                request,"Herramientas/Views.html",{
                    "Herramientas": Herramienta,'Prestamo':Prestamos,
                    "usuario": request.user.username,
                    "Acta":Acta_prestado,
                },
            )

        else:
            return render(
                request,
                "Herramientas/Editar.html",
                {
                    "form": form_acta,
                    "error": "error",
                    "acta": acta,
                    "Edit_acta":"Edit_acta",
                },
            )

@login_required
def confirmacion_eliminar(request,id_articulo):
    resolved_url = resolve(request.path_info).url_name
    if resolved_url == 'confirmar_herramienta':    
        return render(request, "Herramientas/confirmar.html", {"id": id_articulo,"herramienta":"herramienta"})
    else:
        return render(request, "Herramientas/confirmar.html", {"id": id_articulo,"acta":"acta"})
    

    
    
def Eliminar(request, id_articulo):
    
    resolved_url = resolve(request.path_info).url_name
    if resolved_url=='Eliminar_Herramienta':
        herramienta_delete = Herramientas.objects.get(pk=id_articulo)
        #Registramos la eliminacion en movimientos:
        fecha_actual = datetime.now()
        Registro_de_eliminacion = MovimientoUsoDiario(
                    fecha=fecha_actual.strftime("%Y-%m-%d"),
                    accion="Herramienta eliminada",
                    Nombre_de_Articulo=herramienta_delete.nombre,
                    Codigo=0,
                    Cantidad=0,
                    Destino="",
                    Entrega_conforme="",
                    Recibe_conforme=request.user.username,
                )
        Registro_de_eliminacion.save()
        #Guardamos la eliminacion en la base de datos
        herramienta_delete.delete()
    elif resolved_url=="Eliminar_Acta":
        acta_delete= Acta_entrega_herramienta.objects.get(pk=id_articulo)
        #Guardamos la eliminacion en la base de datos
        acta_delete.delete()
    # Le pasamos todos los articulos a la vista inventario
    Herramienta = Herramientas.objects.all().order_by("ubicacion")
    Acta_prestado=Acta_entrega_herramienta.objects.all().order_by("-fecha")
    Prestamos=Prestamo.objects.all().order_by("-acta")
    return render(
        request,"Herramientas/Views.html",{
            "Herramientas": Herramienta,'Prestamo':Prestamos,
            "usuario": request.user.username,
            "Acta":Acta_prestado,
        },
    )
