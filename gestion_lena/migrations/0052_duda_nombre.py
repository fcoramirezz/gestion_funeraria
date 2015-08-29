# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0051_auto_20150828_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='duda',
            name='nombre',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
