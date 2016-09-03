# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0009_auto_20160107_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='destino',
            field=models.ForeignKey(to='viajes.Destino'),
            preserve_default=True,
        ),
    ]
