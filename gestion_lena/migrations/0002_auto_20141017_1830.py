# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingreso',
            old_name='valor',
            new_name='valor_unitario',
        ),
    ]
