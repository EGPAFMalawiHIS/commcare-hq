# Generated by Django 2.2.24 on 2021-09-30 12:35

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_add_edit_messaging_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='changes',
            field=django.contrib.postgres.fields.jsonb.JSONField(
                default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
    ]