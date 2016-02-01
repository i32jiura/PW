from django.utils.decorators import method_decorator

from django.shortcuts import render, redirect, get_object_or_404
from viajes.models import Destino, Viaje, Ruta
from viajes.forms import nuevoDestinoForm, nuevoViajeForm, nuevaRutaForm, autenticacionForm, registroForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View

def inicio(request):
    return render(request,"inicio.html")

def listarDestinos(request):
    destinos=Destino.objects.all()
    contexto={'destinos':destinos}
    return render(request,"destino/listarDestinos.html",contexto)

def detalleDestino(request,destino_id):
    destinoEspecifico=Destino.objects.get(pk=destino_id)
    contexto={'destinoEspecifico':destinoEspecifico}
    return render(request,"destino/detalleDestino.html",contexto)

@login_required(login_url='/login')
def crearDestino(request):
    if request.method=='POST':
        destino=Destino()
        formulario=nuevoDestinoForm(request.POST,instance=destino)
        if formulario.is_valid():
            formulario.save()
            return redirect('/destino')
    else:
        formulario=nuevoDestinoForm()

    contexto={'formulario':formulario}

    return render(request,"destino/crearDestino.html",contexto)

def listarViajes(request):
    viajes=Viaje.objects.all()
    contexto={'viajes':viajes}
    return render(request,"viaje/listarViajes.html",contexto)

def detalleViaje(request,viaje_id):
    viajeEspecifico=Viaje.objects.get(pk=viaje_id)
    contexto={'viajeEspecifico':viajeEspecifico}
    return render(request,"viaje/detalleViaje.html",contexto)

@login_required(login_url='/login')
def crearViaje(request):
    if request.method=='POST':
        viaje=Viaje()
        formulario=nuevoViajeForm(request.POST,instance=viaje)
        if formulario.is_valid():
            formulario.save()
            return redirect('/viaje')
    else:
        formulario=nuevoViajeForm()
    contexto={'formulario':formulario}
    return render(request,"viaje/crearViaje.html",contexto)

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
        return render(request,"viaje/editarViaje.html",contexto)

class listarRutas(View):
    template_nombre="ruta/listarRutas.html"
    def get(self,request,*args,**kwargs):
        rutas=Ruta.objects.all()
        contexto={'rutas':rutas}
        return render(request,self.template_nombre,contexto)

class detalleRuta(View):
    template_nombre="ruta/detalleRuta.html"
    def get(self,request,*args,**kwargs):
        id=self.kwargs['ruta_id']
        rutaEspecifica=get_object_or_404(Ruta,pk=id)
        contexto={'rutaEspecifica':rutaEspecifica}
        return render(request,self.template_nombre,contexto)

class crearRuta(View):
    form_clase=nuevaRutaForm
    template_nombre="ruta/crearRuta.html"

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
            return redirect('/ruta')
        contexto={'formulario':formulario}
        return render(request,self.template_nombre,contexto)

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
                    return redirect('/')
                else:
                    return render(request, 'errorLogin.html')
            else:
                return render(request, 'errorLogin.html')
    else:
        formulario=autenticacionForm()
    contexto={'formulario':formulario}
    return render(request,'login.html',contexto)

@login_required(login_url='/login')
def usuarioLogout(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])

def usuarioRegistro(request):
    if request.method=='POST':
        formulario=registroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/')
    else:
        formulario=registroForm()
    contexto={'formulario':formulario}
    return render(request,'registro.html',contexto)