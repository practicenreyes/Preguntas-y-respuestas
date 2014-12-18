# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('asunto', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('contenido', models.TextField()),
                ('mejor_respuesta', models.BooleanField(default=False, verbose_name='Respuesta preferida')),
                ('pregunta', models.ForeignKey(to='preguntasyrespuestas.Pregunta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
