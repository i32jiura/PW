# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0006_auto_20160107_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='desplazamiento',
            field=models.CharField(max_length=10, choices=[(b'Tren', b'Tren'), (b'Avion', b'Avion'), (b'Barco', b'Barco'), (b'Autobus', b'Autobus')]),
            preserve_default=True,
        ),
    ]
