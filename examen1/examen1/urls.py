from django.conf.urls import patterns, include, url
from django.contrib import admin
from viajes import views
from viajes.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'examen1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.inicio, name='Inicio'),
    url(r'^login/', views.usuarioLogin, name='Login Usuario'),
    url(r'^logout/', views.usuarioLogout, name='Logout Usuario'),
    url(r'^registro/', views.usuarioRegistro, name='Registro Usuario'),

    url(r'^destino/', views.listarDestinos, name='Listar Destinos'),
    url(r'^verDestino/(?P<destino_id>\d+)', views.detalleDestino, name='Detalle Destino'),
    url(r'^crearDestino/', views.crearDestino, name='Crear Destino'),

    url(r'^viaje/', views.listarViajes, name='Listar Viajes'),
    url(r'^verViaje/(?P<viaje_id>\d+)', views.detalleViaje, name='Detalle Viaje'),
    url(r'^crearViaje/', views.crearViaje, name='Crear Viaje'),
    url(r'^editarViaje/(?P<viaje_id>\d+)', views.editarViaje, name='Editar Viaje'),

    url(r'^ruta/', listarRutas.as_view(), name='Listar Rutas'),
    url(r'^verRuta/(?P<ruta_id>\d+)', detalleRuta.as_view(), name='Detalle Ruta'),
    url(r'^crearRuta/', crearRuta.as_view(), name='Crear Ruta'),

    url(r'^admin/', include(admin.site.urls)),
)
