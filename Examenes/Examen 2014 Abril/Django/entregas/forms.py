from entregas.models import *
from django.forms import ModelForm

class DestinatarioForm(ModelForm):
	class Meta:
		model = Destinatario
		
class PaqueteForm(ModelForm):
	class Meta:
		model = Paquete
