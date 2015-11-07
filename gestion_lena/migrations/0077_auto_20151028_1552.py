# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0076_auto_20151028_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duda',
            name='pregunta',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='duda',
            name='respuesta',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='duda',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
    ]
