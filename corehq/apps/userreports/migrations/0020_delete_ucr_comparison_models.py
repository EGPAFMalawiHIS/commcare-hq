# Generated by Django 3.2.18 on 2023-05-22 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userreports', '0019_ucrexpression_upstream_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReportComparisonDiff',
        ),
        migrations.DeleteModel(
            name='ReportComparisonException',
        ),
        migrations.DeleteModel(
            name='ReportComparisonTiming',
        ),
    ]