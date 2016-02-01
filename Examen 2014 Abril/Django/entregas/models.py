from django.db import models

# Create your models here.

class Destinatario (models.Model):
	nombre = models.CharField (max_length = 128)
	direccion = models.CharField (max_length = 128)
	ciudad = models.CharField (max_length = 128)
	codigo_postal = models.IntegerField ()
	def __unicode__(self):
		return (self.nombre)
		
class Paquete (models.Model):
	destinatario = models.ForeignKey (Destinatario)
	contenido = models.TextField ()
	valor = models.IntegerField ()
	
	def __unicode__(self):
		return (self.contenido)			
