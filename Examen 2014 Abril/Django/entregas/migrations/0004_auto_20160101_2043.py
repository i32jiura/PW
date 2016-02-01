# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entregas', '0003_ruta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruta',
            name='paquete',
        ),
        migrations.DeleteModel(
            name='Ruta',
        ),
    ]
