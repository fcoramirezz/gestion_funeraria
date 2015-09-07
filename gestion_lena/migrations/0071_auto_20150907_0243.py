# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0070_auto_20150907_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen_pr',
            field=models.ImageField(default=None, null=True, upload_to=b'media/servicios', blank=True),
        ),
    ]
