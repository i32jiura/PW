# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0005_ruta_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruta',
            name='coste',
        ),
        migrations.RemoveField(
            model_name='ruta',
            name='dias',
        ),
    ]
