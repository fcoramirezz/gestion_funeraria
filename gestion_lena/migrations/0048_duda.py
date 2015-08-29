# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0047_servicio_publicar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta', models.TextField(null=True, blank=True)),
                ('respuesta', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Duda',
                'verbose_name_plural': 'Dudas',
            },
            bases=(models.Model,),
        ),
    ]
