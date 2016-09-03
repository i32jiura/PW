# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinatario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('direccion', models.CharField(max_length=128)),
                ('ciudad', models.CharField(max_length=128)),
                ('codigo_postal', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
