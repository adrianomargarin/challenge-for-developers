# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20171011_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
    ]
