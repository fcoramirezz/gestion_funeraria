# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0004_configuracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='creado_en',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 19, 14, 46, 59, 886591), auto_now_add=True),
            preserve_default=False,
        ),
    ]
