from django.conf.urls import patterns, include, url
from django.contrib import admin
from viajes.views import *
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AgenciaViajes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Indice),
    
    url(r'^Listar/$', VerDestinos),
    url(r'^Listar/Destino/(?P<destino_id>[0-9]+)/$', VerDestino),
    url(r'^AddDestino/$',AddDestino),
    
    url(r'^ListarV/$', VerViajes),
    url(r'^ListarV/Viaje/(?P<viaje_id>[0-9]+)/$', VerViaje),
    url(r'^AddViaje/$',AddViaje),
    url(r'^ListarV/Viaje/(?P<viaje_id>[0-9]+)/EditarViaje/$', EditViaje),
    
    url(r'^ListarR/$', VerRutas),
    url(r'^AddRuta/$', AddRuta),
    url(r'^ListarR/Ruta/(?P<ruta_id>[0-9]+)/$', VerRuta),
    url(r'^ListarR/Ruta/(?P<ruta_id>[0-9]+)/EditarRuta/$', EditRuta),
    
    url(r'^Login/$', log),
    url(r'^Logout/$', exit),
)
