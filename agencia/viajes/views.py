from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic.base import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from viajes.models import *
from viajes.forms import *


# Create your views here.

def inicio(request):
    return render(request,"inicio.html")

def usuarioLogin(request):
	if request.method=='POST':
	    formulario=autenticacionForm(request.POST)
	    if formulario.is_valid:
	        usuario=request.POST['username']
	        clave=request.POST['password']
	        acceso=authenticate(username=usuario, password=clave)
	        if acceso is not None:
	            if acceso.is_active:
	                login(request,acceso)
	                return render(request,"inicio.html")
	            else:
	                return render(request, 'errorLogin.html')
	        else:
	            return render(request, 'errorLogin.html')
	else:
	    formulario=autenticacionForm()
	#contexto={'formulario':formulario}
	return render(request,'login.html',{'formulario':formulario})
       

def listarDestinos(request):
    destinos=Destino.objects.all()
    return render(request,"listarDestinos.html",{'destinos': destinos})    

@login_required(login_url='/login')
def crearDestino(request):
    if request.method=='POST':
        destino=Destino()
        formulario=nuevoDestinoForm(request.POST,instance=destino)
        if formulario.is_valid():
            formulario.save()
            return render(request,"inicio.html")
    else:
        formulario=nuevoDestinoForm()

    #contexto={'formulario':formulario}

    return render(request,"crearDestino.html",{'formulario':formulario})

def detalleDestino(request,destino_id):
    destinoEspecifico=Destino.objects.get(pk=destino_id)
    contexto={'destinoEspecifico':destinoEspecifico}
    return render(request,"detalleDestino.html",contexto)    

#---------------------------------------------------------------------------------------------------
#						VIAJES
#---------------------------------------------------------------------------------------------------

def Viajes(request):
    viajes=Viaje.objects.all()
    return render(request,"listarViajes.html",{'viajes': viajes})


@login_required(login_url='/login')
def crearViaje(request):
    if request.method=='POST':
        viaje=Viaje()
        formulario=nuevoViajeForm(request.POST,instance=viaje)
        if formulario.is_valid():
            formulario.save()
            return render(request,"inicio.html")
    else:
        formulario=nuevoViajeForm()
    contexto={'formulario':formulario}
    return render(request,"crearViaje.html",contexto)

def detalleViaje(request,viaje_id):
    viajeEspecifico=Viaje.objects.get(pk=viaje_id)
    contexto={'viajeEspecifico':viajeEspecifico}
    return render(request,"detalleViaje.html",contexto)

@login_required(login_url='/login')
def editarViaje(request,viaje_id):
    viaje=get_object_or_404(Viaje,pk=viaje_id)
    if request.method=='POST':
        formulario=nuevoViajeForm(request.POST,instance=viaje)
        if formulario.is_valid():
            formulario.save()
            return redirect('/viaje')
    else:
        formulario=nuevoViajeForm(instance=viaje)
        contexto={'formulario':formulario}
        return render(request,"editarViaje.html",contexto)            

#-------------------------------------------------------------------------------------------
#                      RUTAS
#-------------------------------------------------------------------------------------------



class listarRutas(View):
    template_nombre="listarRutas.html"
    def get(self,request,*args,**kwargs):
        rutas=Ruta.objects.all()
        contexto={'rutas':rutas}
        return render(request,self.template_nombre,contexto)

class detalleRuta(View):
    template_nombre="detalleRuta.html"
    def get(self,request,*args,**kwargs):
        id=self.kwargs['ruta_id']
        rutaEspecifica=get_object_or_404(Ruta,pk=id)
        contexto={'rutaEspecifica':rutaEspecifica}
        return render(request,self.template_nombre,contexto)

class crearRuta(View):
    form_clase=nuevaRutaForm
    template_nombre="crearRuta.html"

    @method_decorator(login_required)
    def get(self,request,*args,**kwargs):
        formulario=self.form_clase()
        contexto={'formulario':formulario}
        return render(request,self.template_nombre,contexto)

    @method_decorator(login_required)
    def post(self,request,*args,**kwargs):
        formulario=self.form_clase(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return render(request,'inicio.html')
        contexto={'formulario':formulario}
        return render(request,self.template_nombre,contexto)