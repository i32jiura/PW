from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','principal.views.inicio'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
    url(r'^registro/$','principal.views.registro'),
    url(r'^administrar/$','principal.views.administrar'),
    url(r'^administrar/puntos$','principal.views.admpuntos'),
    url(r'^administrar/fichajes$','principal.views.admfichajes'),
    url(r'^administrar/puntosaleatorios$','principal.views.puntosaleatorios'),
    url(r'^administrar/jugadores$','principal.views.jugadorenbd'),
    url(r'^privado/$','principal.views.privado'),
    url(r'^cerrar/$', 'principal.views.cerrar'),
    url(r'^jugar/$','principal.views.jugar'),
    url(r'^ingresar/$','principal.views.ingresar'),
    url(r'^jugar/clasificacion$','principal.views.clasificacion'),
    url(r'^liga/clasificacion/(?P<id>\d+)$','principal.views.detalle_equipo'),
    url(r'^jugar/equipo$','principal.views.equipo'),
    url(r'^liga/equipo/(?P<id_jugador>\d+)$','principal.views.detalle_jugador'),
    url(r'^jugar/fichajes$','principal.views.fichajes'),
    url(r'^jugar/buscar$','principal.views.buscar'),
)
