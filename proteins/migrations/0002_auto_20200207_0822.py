# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-02-07 08:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proteins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lipopeptideapplicationsdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 8, 22, 7, 293671, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidedata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 8, 22, 7, 292577, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidediscoverdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 8, 22, 7, 298421, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidefunctionsdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 8, 22, 7, 295902, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptideliganddata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 8, 22, 7, 296764, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidemetabolismdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 8, 22, 7, 299402, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidepathwaydata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 8, 22, 7, 297538, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidepropertiesdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 8, 22, 7, 300155, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidereferencesdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 8, 22, 7, 300900, tzinfo=utc)),
        ),
    ]