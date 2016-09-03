from django.db import models

# Create your models here

# Un destino es un lugar al que se puede viajar, pero sin incluir los datos respecto al viaje, como precio, etc...
class Destino(models.Model):
	lugar = models.CharField(max_length=100)
	descripcion = models.TextField()
	distancia = models.IntegerField()
	
	def __unicode__(self):
        	return self.lugar
