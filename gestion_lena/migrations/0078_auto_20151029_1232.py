# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0077_auto_20151028_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen_pr',
            field=models.ImageField(upload_to=b'media/servicios'),
        ),
    ]
