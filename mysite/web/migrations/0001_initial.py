# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Novedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('contenido', models.TextField()),
                ('fechaP', models.DateTimeField(verbose_name=b'fecha de publicacion')),
                ('tags', models.CharField(max_length=30)),
            ],
        ),
    ]