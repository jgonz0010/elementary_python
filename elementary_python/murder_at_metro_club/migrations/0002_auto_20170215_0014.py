# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('murder_at_metro_club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suspect',
            name='attire',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='suspect',
            name='hair',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='suspect',
            name='room',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
