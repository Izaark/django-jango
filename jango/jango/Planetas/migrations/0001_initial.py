# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-06 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number_moons', models.IntegerField(default=0, null=True)),
                ('color', models.CharField(max_length=10)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('era', models.CharField(blank=True, max_length=15)),
                ('habitable', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Planeta',
                'verbose_name_plural': 'Planetas',
            },
        ),
    ]