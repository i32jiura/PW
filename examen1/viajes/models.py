from django.db import models

class Destino(models.Model):
    lugar=models.CharField(max_length=100)
    descripcion=models.TextField()
    distancia=models.IntegerField()

    def __unicode__(self):
        return self.lugar

class Viaje(models.Model):

    MODOS_DESPLAZAMIENTO = (
    ('Tren', 'Tren'),
    ('Avion', 'Avion'),
    ('Barco', 'Barco'),
    ('Autobus', 'Autobus'),
    )

    destino=models.ForeignKey(Destino, related_name="viajes")
    dias=models.IntegerField()
    precio=models.IntegerField()
    desplazamiento=models.CharField(max_length=7,choices=MODOS_DESPLAZAMIENTO,default='Tren')

    def __unicode__(self):
        return self.destino.lugar + " [" + self.desplazamiento + "]"

class Ruta(models.Model):
    nombre=models.CharField(max_length=100)
    destinos=models.ManyToManyField(Destino)

    def __unicode__(self):
        return self.nombre

    def getDias(self):
        dias=0
        for destino in self.destinos.all():
            for viaje in destino.viajes.all():
                dias+=viaje.dias
        return dias

    def getPrecio(self):
        precio=0
        for destino in self.destinos.all():
            for viaje in destino.viajes.all():
                precio+=viaje.precio
        return precio