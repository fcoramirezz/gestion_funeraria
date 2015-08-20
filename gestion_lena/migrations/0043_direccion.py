# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0042_imagen_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
            },
            bases=(models.Model,),
        ),
    ]
