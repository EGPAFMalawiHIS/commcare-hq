# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 21:36
from __future__ import absolute_import, unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icds_reports', '0120_auto_20190529_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icdsfile',
            name='file_added',
            field=models.DateField(auto_now=True, help_text='Date that field was modified'),
        ),
    ]
