from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from eleccion.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from eleccion.models import *

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

#class listarCircunscritos(View):
#    template_nombre="listarCircunscritos.html"
#    def get(self,request,*args,**kwargs):
#        Circunscritos=Circunscrito.objects.all()
#        contexto={'circunscritos':circunscritos}
#        return render(request,self.template_nombre,contexto)