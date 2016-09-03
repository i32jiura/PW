from django.db import models

# Create your models here.

# Un destino es un lugar al que se puede viajar, pero sin incluir los datos respecto al viaje, como precio, etc...
class Destino(models.Model):
	lugar = models.CharField(max_length=100)
	descripcion = models.TextField()
	distancia = models.IntegerField()
	
	def __unicode__(self):
        	return self.lugar
        	
class Viaje(models.Model):
	destino = models.ForeignKey(Destino, related_name="viajes")
	dias = models.IntegerField()
	coste = models.IntegerField()
	
	OPCIONES = (
	('Tren','Tren'),
	('Avion','Avion'),
	('Barco','Barco'),
	('Autobus','Autobus'),
	)
	
	desplazamiento = models.CharField(max_length=10, choices = OPCIONES)
	
	def __str__(self):
		return self.destino
		
class Ruta(models.Model):
	nombre = models.CharField(max_length=200)
	destinos = models.ManyToManyField(Destino)
	
	def __str__(self):
		return self.nombre
		
	def getDias(self):
		dias=0
		for destino in self.destinos.all():
			for viaje in destino.viajes.all():
				dias+=viaje.dias
		return dias
		
	def getCoste(self):
		coste=0
		for destino in self.destinos.all():
			for viaje in destino.viajes.all():
				coste+=viaje.coste
		return coste		
	
