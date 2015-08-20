# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0028_remove_pedido_valor_unitario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_foto', models.CharField(max_length=255)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['creado_en'],
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Im\xe1genes',
            },
            bases=(models.Model,),
        ),
    ]
