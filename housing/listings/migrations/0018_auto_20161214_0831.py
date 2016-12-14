# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_auto_20161214_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='Image')),
            ],
        ),
        migrations.RemoveField(
            model_name='listing',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='image3',
        ),
        migrations.AddField(
            model_name='images',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='listings.Listing'),
        ),
    ]
