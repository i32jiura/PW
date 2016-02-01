# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0004_auto_20160103_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='nombre',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
