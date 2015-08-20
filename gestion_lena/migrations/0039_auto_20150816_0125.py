# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0038_trabajador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sueldo',
            name='trabajador',
            field=models.ForeignKey(to='gestion_lena.Trabajador'),
        ),
    ]
