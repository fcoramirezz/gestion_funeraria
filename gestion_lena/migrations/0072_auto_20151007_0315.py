# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0071_auto_20150907_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='arreglo_floral',
            field=models.CharField(default=b'Peque\xc3\xb1o', max_length=100, choices=[(b'Peque\xc3\xb1o', b'Peque\xc3\xb1o'), (b'Mediano', b'Mediano'), (b'Grande', b'Grande')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicio',
            name='aviso_prensa',
            field=models.CharField(default=b'No', max_length=100, choices=[(b'Si', b'Si'), (b'No', b'No')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicio',
            name='carroza_flores',
            field=models.CharField(default=b'No', max_length=100, choices=[(b'Si', b'Si'), (b'No', b'No')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicio',
            name='tipo_urna',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
