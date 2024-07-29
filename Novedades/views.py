from django.shortcuts import render
from .models import Novedad
from .form import FormNovedad
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

    
@login_required
def Novedad_View(request):
    
    if request.method == "GET":
        busqueda = request.GET.get("Buscar", "")
        mayor_o_menor=5
        if busqueda:
            ViewNovedades = Novedad.objects.filter(
                Q(fecha__icontains=busqueda)
                | Q(usuario__icontains=busqueda)
                | Q(Texto__icontains=busqueda)
            ).distinct()
            mayor_o_menor=10
            form_Ingreso = FormNovedad()
            form_Ingreso.fields["usuario"].initial=request.user.username
        else:   
            ViewNovedades = Novedad.objects.all().order_by("-id")
            form_Ingreso = FormNovedad()
            form_Ingreso.fields["usuario"].initial=request.user.username
        return render(
            request,
            "Novedades/Novedad.html",
            {
                "Novedades": ViewNovedades,
                'form':form_Ingreso, 
                "mayor_o_menor":mayor_o_menor,
                "GERMAN":"GERMAN"
                },
        )
    else:
        # Procesamos la informacion si es valida lo guardamos
        form_Ingreso = FormNovedad(request.POST)
        if form_Ingreso.is_valid():
            form_Ingreso.save()
            form_Ingreso = FormNovedad()
            form_Ingreso.fields["usuario"].initial=request.user.username
            ViewNovedades = Novedad.objects.all().order_by("-id")
            return render(request,"Novedades/Novedad.html",{"Novedades": ViewNovedades,'form':form_Ingreso},)
        ViewNovedades = Novedad.objects.all().order_by("-id")
        form_Ingreso = FormNovedad()
        form_Ingreso.fields["usuario"].initial=request.user.username
        return render(
            request, "Novedades/Novedad.html", {"Novedades": ViewNovedades,
                                                "form": form_Ingreso, 
                                                "error": "error",
                                                "GERMAN":"GERMAN"}
        )
    
@login_required
def Eliminar_Novedad(request, Novedad_id):
    
    Novedad_delete = Novedad.objects.get(pk=Novedad_id)
    Novedad_delete.delete()
    if request.method == "GET":
        busqueda = request.GET.get("Buscar", "")
        mayor_o_menor=5
        if busqueda:
            ViewNovedades = Novedad.objects.filter(
                Q(fecha__icontains=busqueda)
                | Q(usuario__icontains=busqueda)
                | Q(Texto__icontains=busqueda)
            ).distinct()
            mayor_o_menor=10
            form_Ingreso = FormNovedad()
            form_Ingreso.fields["usuario"].initial=request.user.username
        else:   
            ViewNovedades = Novedad.objects.all().order_by("-id")
            form_Ingreso = FormNovedad()
            form_Ingreso.fields["usuario"].initial=request.user.username
        return render(
            request,
            "Novedades/Novedad.html",
            {
                "Novedades": ViewNovedades,
                'form':form_Ingreso, 
                "mayor_o_menor":mayor_o_menor,
                "GERMAN":"GERMAN"
                },
        )
    
    
