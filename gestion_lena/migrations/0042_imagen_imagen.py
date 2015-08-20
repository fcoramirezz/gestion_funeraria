# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0041_auto_20150816_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'media'),
            preserve_default=True,
        ),
    ]
