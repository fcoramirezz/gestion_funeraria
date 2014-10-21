# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0008_auto_20141020_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='numero',
            field=models.CharField(max_length=10),
        ),
    ]
