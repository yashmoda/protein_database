# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-02-28 07:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proteins', '0004_auto_20200207_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lipopeptideliganddata',
            name='is_already_bound',
        ),
        migrations.RemoveField(
            model_name='lipopeptideliganddata',
            name='ligand_position',
        ),
        migrations.RemoveField(
            model_name='lipopeptidemetabolismdata',
            name='metabolism_description',
        ),
        migrations.AddField(
            model_name='lipopeptidemetabolismdata',
            name='metabolism_model',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lipopeptidemetabolismdata',
            name='metabolism_probability',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='lipopeptidemetabolismdata',
            name='metabolism_result',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lipopeptidepropertiesdata',
            name='property_value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lipopeptideapplicationsdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 8, 17, 9402, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidedata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 8, 17, 8139, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidediscoverdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 8, 17, 14903, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidefunctionsdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 8, 17, 12351, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptideliganddata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 8, 17, 13193, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidemetabolismdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 8, 17, 15911, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidepathwaydata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 8, 17, 14005, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidepropertiesdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 8, 17, 16652, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidereferencesdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 7, 8, 17, 17457, tzinfo=utc)),
        ),
    ]
