# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-02-28 07:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proteins', '0006_auto_20200228_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='lipopeptidemetabolismdata',
            name='metabolism_units',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lipopeptidemetabolismdata',
            name='metabolism_value',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='lipopeptideapplicationsdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 25, 11, 750727, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidedata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 25, 11, 749842, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidediscoverdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 25, 11, 755074, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidefunctionsdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 25, 11, 752859, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptideliganddata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 25, 11, 753578, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidemetabolismdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 25, 11, 756087, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidepathwaydata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 25, 11, 754266, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidepropertiesdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 25, 11, 756837, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidereferencesdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 25, 11, 757495, tzinfo=utc)),
        ),
    ]
