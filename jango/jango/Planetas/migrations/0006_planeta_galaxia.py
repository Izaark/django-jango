# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-07 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Planetas', '0005_galaxia'),
    ]

    operations = [
        migrations.AddField(
            model_name='planeta',
            name='galaxia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='planeta_galaxia', to='Planetas.Galaxia'),
            preserve_default=False,
        ),
    ]
