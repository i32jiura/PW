# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0004_auto_20160104_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='saldo',
            new_name='objeto',
        ),
        migrations.RenameField(
            model_name='articulo',
            old_name='horas',
            new_name='servicio',
        ),
    ]
