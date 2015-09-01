# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0058_auto_20150901_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='imagen_sec3',
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen_pr',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen_sec1',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen_sec2',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
        ),
    ]
