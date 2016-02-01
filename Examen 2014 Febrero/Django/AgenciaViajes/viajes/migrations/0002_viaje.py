# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dias', models.CharField(max_length=200)),
                ('coste', models.IntegerField()),
                ('desplazamiento', models.TextField()),
                ('destino', models.ForeignKey(to='viajes.Destino')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
