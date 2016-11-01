# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-29 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_listing_listing_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='laundry',
        ),
        migrations.AlterField(
            model_name='listing',
            name='additional_lease_terms',
            field=models.TextField(blank=True, default='', help_text='Example: Owner pays for trash and sewer. Tenant responsible for gas and electric. Owner shovel snow, lawn, garden, driveway maintenance'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='furnished',
            field=models.CharField(choices=[('none', 'Unfurnished'), ('lightly_furnished', 'Lightly furnished'), ('fully_furnished', 'Fully furnished')], max_length=17),
        ),
        migrations.AlterField(
            model_name='listing',
            name='parking_space_count',
            field=models.CharField(choices=[('0', 'None'), ('1', '1'), ('2', '2'), ('3_plus', '3+')], max_length=2),
        ),
    ]