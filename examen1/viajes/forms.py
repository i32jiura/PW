from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from viajes.models import Destino, Viaje, Ruta
from django.contrib.auth.forms import UserCreationForm

class nuevoDestinoForm(forms.ModelForm):
    class Meta:
        model=Destino
        fields=['lugar','descripcion','distancia']

class nuevoViajeForm(forms.ModelForm):
    class Meta:
        model=Viaje
        fields=['destino','dias','precio','desplazamiento']

class nuevaRutaForm(forms.ModelForm):
    class Meta:
        model=Ruta
        fields=['nombre','destinos']

class autenticacionForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={'password': forms.PasswordInput(),}

class registroForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username']