# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housinguser',
            name='phone',
        ),
    ]