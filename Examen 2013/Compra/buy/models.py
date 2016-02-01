from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(User):
	saldo = models.FloatField(default = 0.0,null=True)
	horas = models.IntegerField(default = 0, null = True)	
	
class Articulo(models.Model):
	nombre = models.CharField(max_length=120)
	usuario = models.ForeignKey(Perfil)
	objeto = models.FloatField(default = 0.0,null=True)
	servicio = models.IntegerField(default = 0, null = True)				
