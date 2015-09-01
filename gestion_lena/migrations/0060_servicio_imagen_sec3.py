# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0059_auto_20150901_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='imagen_sec3',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
            preserve_default=True,
        ),
    ]
