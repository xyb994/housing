# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_auto_20161213_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housinguser',
            name='phone',
            field=models.CharField(blank=True, default='0000000000', max_length=15),
        ),
    ]