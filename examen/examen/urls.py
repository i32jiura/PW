from django.conf.urls import patterns, include, url
from django.contrib import admin
from eleccion.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'examen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','eleccion.views.inicio'),
    url(r'^verCircunscritos/',ListarCircunscritos.as_view()),
    url(r'^verMesas/','eleccion.views.VerMesas'),
    url(r'^login/','eleccion.views.Login'),
    url(r'^AddMesa/','eleccion.views.addMesa'),
    url(r'^verCircunscrito/(?P<circunscrito_id>\d+)', detalleCirc.as_view(), name='Detalle circuns'),
    url(r'^crearCircunscrito/', crearCircunscrito.as_view(), name='Crear Circunscrito'),
)
