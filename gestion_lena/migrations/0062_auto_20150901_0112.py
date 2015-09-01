# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0061_auto_20150901_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen_pr',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
        ),
    ]
