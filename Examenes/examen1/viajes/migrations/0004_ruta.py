# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0003_auto_20160104_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dias', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('destinos', models.ManyToManyField(to='viajes.Destino')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
