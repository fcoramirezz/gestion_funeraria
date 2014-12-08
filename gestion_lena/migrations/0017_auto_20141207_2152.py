# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0016_huellacarbono'),
    ]

    operations = [
        migrations.AddField(
            model_name='huellacarbono',
            name='kilowatt',
            field=models.DecimalField(default=0.45, max_digits=8, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='huellacarbono',
            name='kilometro',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
    ]
