# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-06 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planetas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planeta',
            name='era',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
