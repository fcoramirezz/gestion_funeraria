# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0039_auto_20150816_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='tipo_de_contacto',
        ),
    ]
