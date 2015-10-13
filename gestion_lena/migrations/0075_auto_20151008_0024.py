# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0074_auto_20151007_0326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='aviso_prensa',
            new_name='aviso_de_prensa',
        ),
    ]
