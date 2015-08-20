# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0031_auto_20150809_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sueldo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('comentario', models.TextField(null=True, blank=True)),
                ('fecha', models.DateField()),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('trabajador', models.ForeignKey(to='gestion_lena.Contacto')),
            ],
            options={
                'verbose_name': 'Sueldo',
                'verbose_name_plural': 'Sueldos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='sueldo',
            field=models.OneToOneField(null=True, blank=True, to='gestion_lena.Sueldo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='tipo_de_contacto',
            field=models.IntegerField(default=3, choices=[(0, b'Proveedor'), (1, b'Cliente'), (2, b'Trabajador'), (3, b'Otro')]),
        ),
    ]
