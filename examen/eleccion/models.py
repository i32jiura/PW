from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Circunscrito(models.Model):
	nombre=models.CharField(max_length=100)
	escanyos=models.IntegerField()
	def get_absolute_url(self):
		return reverse('author-detail', kwargs={'pk': self.pk})
	def __unicode__(self):
		return self.nombre

class Mesa(models.Model):
	nombre=models.CharField(max_length=100)
	recuento=models.IntegerField()
	circunscrito=models.ForeignKey(Circunscrito)
	def __unicode__(self):
		return (self.nombre)

class Partido(models.Model):
	mesa=models.ForeignKey(Mesa)
	nombre=models.CharField(max_length=100)
	escanyos=models.IntegerField()

class Resultado(models.Model):
	partido=models.OneToOneField(Partido)
	mesa=models.OneToOneField(Mesa)
	votos=models.IntegerField()