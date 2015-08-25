# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0045_auto_20150817_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='creado_en',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
