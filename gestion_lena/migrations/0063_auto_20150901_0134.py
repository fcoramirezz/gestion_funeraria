# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0062_auto_20150901_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen_sec1',
            field=models.FileField(null=True, upload_to=b'media', blank=True),
        ),
    ]
