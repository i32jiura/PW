# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0008_auto_20160107_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='dias',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
