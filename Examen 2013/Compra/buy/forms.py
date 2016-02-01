from buy.models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class CreatePerfil(UserCreationForm):
	class Meta:
		model = Perfil
		fields = ('username', 'saldo','horas')
		
class ArticuloForm(ModelForm):
	class Meta:
		model = Articulo		
