# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-14 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earth', '0016_location_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='origin',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='\ucd94\ucd9c\uacbd\ub85c'),
        ),
    ]