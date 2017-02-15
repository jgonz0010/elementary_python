# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suspect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hair', models.CharField(max_length=50)),
                ('attire', models.CharField(max_length=50)),
                ('room', models.IntegerField(default=0)),
                ('is_murderer', models.BooleanField(default=False)),
            ],
        ),
    ]
