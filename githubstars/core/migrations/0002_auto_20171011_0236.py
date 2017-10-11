# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repository',
            options={'verbose_name': 'Repositório', 'verbose_name_plural': 'Repositórios'},
        ),
        migrations.AddField(
            model_name='repository',
            name='language',
            field=models.CharField(default='', max_length=255, verbose_name='Linguagem'),
            preserve_default=False,
        ),
    ]
