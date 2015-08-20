# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0040_remove_contacto_tipo_de_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(default=b'No Pagado', max_length=100, choices=[(b'No Pagado', b'No Pagado'), (b'Pagado', b'Pagado')]),
        ),
    ]
