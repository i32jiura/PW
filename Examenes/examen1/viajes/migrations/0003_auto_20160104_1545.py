# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0002_viaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='desplazamiento',
            field=models.CharField(default=b'Tren', max_length=7, choices=[(b'Tren', b'Tren'), (b'Avion', b'Avion'), (b'Barco', b'Barco'), (b'Autobus', b'Autobus')]),
        ),
    ]
