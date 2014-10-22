# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0012_gasto_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasto',
            name='fecha',
            field=models.DateField(default=datetime.date(2014, 10, 22)),
            preserve_default=False,
        ),
    ]
