# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0003_auto_20160104_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='objeto',
        ),
        migrations.DeleteModel(
            name='Objeto',
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='servicio',
        ),
        migrations.DeleteModel(
            name='Servicio',
        ),
        migrations.AddField(
            model_name='articulo',
            name='horas',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo',
            name='saldo',
            field=models.FloatField(default=0.0, null=True),
            preserve_default=True,
        ),
    ]
