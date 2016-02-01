# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0002_articulo_objeto_servicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objeto',
            name='articulo',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='articulo',
        ),
        migrations.AddField(
            model_name='articulo',
            name='objeto',
            field=models.ForeignKey(default=4, to='buy.Objeto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articulo',
            name='servicio',
            field=models.ForeignKey(default=6, to='buy.Servicio'),
            preserve_default=False,
        ),
    ]
