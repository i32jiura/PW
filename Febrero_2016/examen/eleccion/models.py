from django.db import models

# Create your models here.
class Circunscrito(models.Model):
	nombre=models.CharField(max_length=100)
	escanyos=models.IntegerField()
	def __unicode__(self):
		return self.nombre

class Mesa(models.Model):
	nombre=models.CharField(max_length=100)
	recuento=models.IntegerField()
	circunscrito=models.ForeignKey(Circunscrito)

class Partido(models.Model):
	mesa=models.ForeignKey(Mesa)
	nombre=models.CharField(max_length=100)
	escanyos=models.IntegerField()

class Resultado(models.Model):
	partido=models.OneToOneField(Partido)
	mesa=models.OneToOneField(Mesa)
	votos=models.IntegerField()