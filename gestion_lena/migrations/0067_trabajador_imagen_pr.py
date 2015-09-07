# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0066_auto_20150904_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='imagen_pr',
            field=models.ImageField(null=True, upload_to=b'media'),
            preserve_default=True,
        ),
    ]
