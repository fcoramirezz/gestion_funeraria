# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0003_auto_20141019_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_sistema', models.CharField(max_length=255)),
                ('footer', models.CharField(max_length=255, null=True, blank=True)),
                ('precio_lena', models.PositiveIntegerField()),
                ('carga_maxima_dia', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
