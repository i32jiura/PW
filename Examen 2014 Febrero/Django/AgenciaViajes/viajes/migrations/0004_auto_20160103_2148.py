# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0003_ruta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruta',
            name='destino',
        ),
        migrations.AddField(
            model_name='ruta',
            name='destinos',
            field=models.ManyToManyField(to='viajes.Destino'),
            preserve_default=True,
        ),
    ]
