# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0004_ruta'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='nombre',
            field=models.CharField(default=datetime.date(2016, 1, 4), max_length=100),
            preserve_default=False,
        ),
    ]
