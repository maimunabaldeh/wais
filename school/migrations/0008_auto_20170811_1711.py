# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_auto_20170811_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, default=0, max_length=400),
            preserve_default=False,
        ),
    ]
