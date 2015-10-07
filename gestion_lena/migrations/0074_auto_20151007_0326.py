# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0073_auto_20151007_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='arreglo_floral',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Chico', b'Chico'), (b'Mediano', b'Mediano'), (b'Grande', b'Grande')]),
        ),
    ]
