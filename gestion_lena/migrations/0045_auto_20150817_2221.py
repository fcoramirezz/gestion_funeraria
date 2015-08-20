# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0044_delete_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='direccion_de_ceremonia',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='direccion_de_sepultacion',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='direccion_de_velorio',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='direccion_destino',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
