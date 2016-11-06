# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-03 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
                ('compra', models.DateField(auto_now_add=True)),
                ('caducidad', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Gato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField(blank=True, default=0)),
                ('callejero', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Gato',
                'verbose_name_plural': 'Gatos',
            },
        ),
    ]
