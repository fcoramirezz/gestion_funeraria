# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('tipo_telefono', models.IntegerField(default=2, choices=[(0, b'Movil'), (1, b'Fijo'), (2, b'No Menciona')])),
                ('telefono', models.IntegerField(null=True, blank=True)),
                ('direccion', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=75, null=True, blank=True)),
                ('feha_de_registro', models.DateTimeField(auto_now_add=True)),
                ('ultima_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.IntegerField()),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.IntegerField()),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('direccion_destino', models.CharField(max_length=255)),
                ('estado', models.CharField(default=b'En Proceso', max_length=100, choices=[(b'En Proceso', b'En Proceso'), (b'Entregado', b'Entregado')])),
                ('fecha_entrega', models.DateTimeField(null=True, blank=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('contacto', models.ForeignKey(to='gestion_lena.Contacto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoGasto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='pedido',
            field=models.OneToOneField(to='gestion_lena.Pedido'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gasto',
            name='tipo_gasto',
            field=models.ForeignKey(to='gestion_lena.TipoGasto'),
            preserve_default=True,
        ),
    ]
