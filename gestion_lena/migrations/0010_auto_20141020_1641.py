# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0009_auto_20141020_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='comuna',
            field=models.ForeignKey(default=1, to='gestion_lena.Comuna'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='provincia',
            field=models.ForeignKey(default=1, to='gestion_lena.Provincia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='region',
            field=models.ForeignKey(default=1, to='gestion_lena.Region'),
            preserve_default=False,
        ),
    ]
