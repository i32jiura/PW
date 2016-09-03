from django.conf.urls import patterns, include, url
from django.contrib import admin
from viajes.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agencia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', inicio, name='Inicio'),
    url(r'^inicio', '/', name='Inicio'),
    url(r'^destinos/',listarDestinos, name='Listar Destinos'),
    url(r'^crearDestinos/',crearDestino, name='Crear Destinos'),
    url(r'^login/',usuarioLogin, name='Login'),
    url(r'^verDestino/(?P<destino_id>\d+)',detalleDestino, name='Destino'),
    url(r'^listarViajes/',Viajes, name='Listar viajes'),
    url(r'^viaje/',crearViaje, name='Crear viaje'),
    url(r'^verViaje/(?P<viaje_id>\d+)', detalleViaje, name='Detalle Viaje'),
    url(r'^editarViaje/(?P<viaje_id>\d+)', editarViaje, name='Editar Viaje'),
    url(r'^ruta/', listarRutas.as_view(), name='Listar Rutas'),
    url(r'^verRuta/(?P<ruta_id>\d+)', detalleRuta.as_view(), name='Detalle Ruta'),
    url(r'^crearRuta/', crearRuta.as_view(), name='Crear Ruta'),    
)
