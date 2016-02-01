from django.conf.urls import patterns, include, url
from django.contrib import admin
from entregas.views import *
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index),
    
    url(r'^Destinatarios/$', VerDestinatarios),
    url(r'^AddDestinatario/$', AddDestinatario),
    url(r'^Destinatarios/(?P<destinatario_id>[0-9]+)/$', VerDestinatario),
    
    url(r'^Paquetes/$', VerPaquetes),
    url(r'^AddPaquete/$', AddPaquete),
    url(r'^Paquetes/(?P<paquete_id>[0-9]+)/$', VerPaquete),
    url(r'^Paquetes/(?P<paquete_id>[0-9]+)/EditPaquete/$', EditPaquete),
    
    url(r'^Iniciar-Sesion/$', Login),
    url(r'^Salir/$', Logout),
    
    url(r'^Error/$', TemplateView.as_view(template_name='Error.html')),
)
