from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic.base import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from eleccion.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from eleccion.models import *

def inicio(request):
    circunscritos = Circunscrito.objects.all()
    return render_to_response('base.html',{'circunscritos': circunscritos}, context_instance=RequestContext(request))



def Login(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		user = request.POST['username']
		passw = request.POST['password']
		access = authenticate(username=user,password=passw)
		if access is not None:
			login(request,access)
			return HttpResponseRedirect('/')
	else:
		formulario = AuthenticationForm()
		return render_to_response('login.html',{'formulario':formulario},context_instance=RequestContext(request))


class crearCircunscrito(View):
	form_class=circunscritoForm
	template_name="crearCircunscrito.html"

	@method_decorator(login_required)
	def get(self,request,*args,**kwargs):
		formulario=self.form_class()
		context={'formulario':formulario}
		return render(request,self.template_name,context)
	@method_decorator(login_required)
	def post(self,request,*args,**kwargs):
		formulario=self.form_class(request.POST,request.FILES)
		if formulario.is_valid():
			formulario.save()
			return redirect('/')
		context={'formulario':formulario}
		return render(request,self.template_name,context)


class ListarCircunscritos(View):
    template_name="listarCircunscritos.html"
    def get(self,request,*args,**kwargs):
    	#Comprobar si es superusuario ( con request.user.is_staff se comprueba si es del staff)
    	if request.user.is_superuser:
    		print "Admin"
        circunscritos=Circunscrito.objects.all()
        contex={'circunscritos':circunscritos}
        return render(request,self.template_name,contex)

class detalleCirc(View):
    template_nombre="circunscritoDetalle.html"
    def get(self,request,*args,**kwargs):
        id=self.kwargs['circunscrito_id']
        circuns=get_object_or_404(Circunscrito,pk=id)
        contexto={'circuns':circuns}
        return render(request,self.template_nombre,contexto)

def addMesa(request):
	if request.method == 'POST':
		formulario = MesaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = MesaForm()
		return render_to_response('AddMesa.html',{'formulario':formulario},context_instance=RequestContext(request))

def VerMesas(request):
	mesas = Mesa.objects.all()
	return render_to_response('listarMesas.html',{'mesas':mesas})

def VerPaquete(request,paquete_id):
	paquete = Paquete.objects.get(pk=paquete_id)
	return render_to_response('paquete.html',{'paquete':paquete})
