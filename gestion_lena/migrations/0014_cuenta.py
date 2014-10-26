# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0013_gasto_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('cargo', models.IntegerField()),
                ('abono', models.IntegerField()),
                ('saldo', models.IntegerField(null=True, blank=True)),
                ('gasto', models.OneToOneField(null=True, blank=True, to='gestion_lena.Gasto')),
                ('pedido', models.OneToOneField(null=True, blank=True, to='gestion_lena.Pedido')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
