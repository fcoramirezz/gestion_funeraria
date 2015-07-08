# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0022_auto_20150702_0249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Componentes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_de_componente', models.CharField(max_length=255)),
                ('costo', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('precio_de_venta', models.PositiveIntegerField()),
                ('costo_de_servicio', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tipo_de_servicio',
            field=models.CharField(default=b'F\xc3\xbanebre Tradicional', max_length=100, choices=[(b'Cremacion', b'Cremacion'), (b'Funebre Tradicional', b'Funebre Tradicional'), (b'Otro', b'Otro')]),
        ),
    ]
