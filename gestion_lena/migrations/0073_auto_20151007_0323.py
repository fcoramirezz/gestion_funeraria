# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0072_auto_20151007_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='arreglo_floral',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Peque\xc3\xb1o', b'Peque\xc3\xb1o'), (b'Mediano', b'Mediano'), (b'Grande', b'Grande')]),
        ),
    ]
