from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from buy.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from buy.models import *

# Create your views here.

def Index(request):
	if request.user.is_anonymous():
		usuario = request.user
	else:
		usuario = Perfil.objects.get(username=request.user.username)
	usuarios = Perfil.objects.all()
	articulos = Articulo.objects.all()
	return render_to_response('index.html',{'usuario':usuario, 'usuarios':usuarios, 'articulos':articulos})
	
@login_required(login_url='/')		
def Registrarse(request):
	if request.method == 'POST':
		formulario = CreatePerfil(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = CreatePerfil()
	return render_to_response('register.html',{'formulario':formulario},context_instance=RequestContext(request))
	
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
	
@login_required(login_url='/')
def Salir(request):
	logout(request)
	return HttpResponseRedirect('/')
	
def VerUsuario(request,usuario_id):
	usuario = Perfil.objects.get(pk=usuario_id)
	return render_to_response('VerUsuario.html',{'usuario':usuario})
	
@login_required(login_url='/')	
def AddArticulo(request):
	if request.method == 'POST':
		formulario = ArticuloForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = ArticuloForm()
	return render_to_response('AddArticulo.html',{'formulario':formulario},context_instance=RequestContext(request))
	
def VerArticulo(request,articulo_id):
	usuario = request.user
	articulo = Articulo.objects.get(pk=articulo_id)
	return render_to_response('VerArticulo.html',{'articulo':articulo, 'usuario':usuario})
	
def Comprar(request,articulo_id):
	comprador = Perfil.objects.get(username=request.user.username)
	articulo = Articulo.objects.get(pk=articulo_id)
	vendedor = articulo.usuario
	
	if comprador.saldo >= articulo.objeto and comprador.horas >= articulo.servicio and comprador.username != vendedor.username:
		vendedor.saldo = vendedor.saldo + articulo.objeto
		vendedor.horas = vendedor.horas + articulo.servicio
	
		comprador.saldo = comprador.saldo - articulo.objeto
		comprador.horas = comprador.horas - articulo.servicio
		
		comprador.save()
		vendedor.save()
		articulo.delete()
		
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')
	
				
