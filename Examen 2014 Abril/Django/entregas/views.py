from django.shortcuts import render, render_to_response
from entregas.models import *
from django.http import HttpResponseRedirect
from django.template import RequestContext
from entregas.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
# Create your views here.

def Index(request):
	usuario = request.user
	return render_to_response('index.html',{'usuario':usuario})
	
def VerDestinatarios(request):
	usuario = request.user
	destinatarios = Destinatario.objects.all()
	return render_to_response('destinatarios.html',{'destinatarios':destinatarios, 'usuario':usuario})

@login_required(login_url='/Error')	
def AddDestinatario(request):
	destinatario = Destinatario()
	if request.method == 'POST':
		formulario = DestinatarioForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = DestinatarioForm()
	return render_to_response('AddDestino.html', {'formulario':formulario}, context_instance = RequestContext(request))
	
def VerDestinatario(request,destinatario_id):
	destinatario = Destinatario.objects.get(pk=destinatario_id)
	return render_to_response('destinatario.html', {'destinatario':destinatario})
	
def VerPaquetes(request):
	paquetes = Paquete.objects.all()
	return render_to_response('paquetes.html',{'paquetes':paquetes})

@login_required(login_url='/Error')	
def AddPaquete(request):
	paquete = Paquete()
	if request.method == 'POST':
		formulario = PaqueteForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = PaqueteForm()
	return render_to_response('AddPaquete.html',{'formulario':formulario},context_instance=RequestContext(request))
	
def VerPaquete(request,paquete_id):
	paquete = Paquete.objects.get(pk=paquete_id)
	return render_to_response('paquete.html',{'paquete':paquete})
	
def EditPaquete(request,paquete_id):
	paquete = Paquete.objects.get(pk=paquete_id)
	if request.method == 'POST':
		formulario = PaqueteForm(request.POST,instance = paquete)
		if formulario.is_valid():
			formulario.save()
			url = '/Paquetes/' + paquete_id
			return HttpResponseRedirect(url)
	else:
		formulario = PaqueteForm(instance = paquete)
	return render_to_response('AddPaquete.html',{'formulario':formulario},context_instance=RequestContext(request))
	
def Login(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		user = request.POST['username']
		passw = request.POST['password']
		access = authenticate(username = user, password = passw)
		if access is not None:
			login(request,access)
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/')
	else:
		formulario = AuthenticationForm()
		
	return render_to_response('Login.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/Error')	
def Logout(request):
	logout(request)
	return HttpResponseRedirect('/')
		

						
