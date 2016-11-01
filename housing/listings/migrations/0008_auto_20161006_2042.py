# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-06 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20161006_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bathroom_count',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedroom_count',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='lease_deposit',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='lease_monthly_cost',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='unit_floor',
            field=models.PositiveSmallIntegerField(),
        ),
    ]