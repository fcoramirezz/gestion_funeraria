# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0029_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='detalles_del_servicio',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
