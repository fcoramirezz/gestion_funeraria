# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0037_auto_20150810_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('tipo_telefono', models.IntegerField(default=2, choices=[(0, b'Movil'), (1, b'Fijo'), (2, b'No Menciona')])),
                ('telefono', models.IntegerField(null=True, blank=True)),
                ('direccion', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=75, null=True, blank=True)),
                ('feha_de_registro', models.DateTimeField(auto_now_add=True)),
                ('ultima_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['apellido'],
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
            },
            bases=(models.Model,),
        ),
    ]
