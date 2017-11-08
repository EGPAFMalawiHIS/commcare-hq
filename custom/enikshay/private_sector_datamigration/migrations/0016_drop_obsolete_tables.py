# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-15 15:46
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_sector_datamigration', '0015_add_july_19'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adherence_jul13',
            name='beneficiaryId',
        ),
        migrations.RemoveField(
            model_name='adherence_jun14',
            name='beneficiaryId',
        ),
        migrations.RemoveField(
            model_name='adherence_jun30',
            name='beneficiaryId',
        ),
        migrations.DeleteModel(
            name='Agency_Jul13',
        ),
        migrations.DeleteModel(
            name='Episode_Jul13',
        ),
        migrations.DeleteModel(
            name='Episode_Jun14',
        ),
        migrations.DeleteModel(
            name='Episode_Jun30',
        ),
        migrations.DeleteModel(
            name='EpisodePrescription_Jul13',
        ),
        migrations.DeleteModel(
            name='EpisodePrescription_Jun14',
        ),
        migrations.DeleteModel(
            name='EpisodePrescription_Jun30',
        ),
        migrations.DeleteModel(
            name='UserDetail_Jul13',
        ),
        migrations.DeleteModel(
            name='Voucher_Jul13',
        ),
        migrations.DeleteModel(
            name='Voucher_Jun14',
        ),
        migrations.DeleteModel(
            name='Voucher_Jun30',
        ),
        migrations.DeleteModel(
            name='Adherence_Jul13',
        ),
        migrations.DeleteModel(
            name='Adherence_Jun14',
        ),
        migrations.DeleteModel(
            name='Adherence_Jun30',
        ),
        migrations.DeleteModel(
            name='Beneficiary_Jul13',
        ),
        migrations.DeleteModel(
            name='Beneficiary_Jun14',
        ),
        migrations.DeleteModel(
            name='Beneficiary_Jun30',
        ),
    ]
