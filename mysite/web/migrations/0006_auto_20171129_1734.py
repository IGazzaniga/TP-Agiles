# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20171126_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novedad',
            name='titulo',
            field=models.CharField(max_length=20),
        ),
    ]
