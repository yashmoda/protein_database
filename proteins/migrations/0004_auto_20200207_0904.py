# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-02-07 09:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proteins', '0003_auto_20200207_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lipopeptideapplicationsdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 9, 4, 46, 871893, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidedata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 9, 4, 46, 871013, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidedata',
            name='lipopeptide_structure_2d',
            field=models.ImageField(blank=True, null=True, upload_to='structures/2d/'),
        ),
        migrations.AlterField(
            model_name='lipopeptidedata',
            name='lipopeptide_structure_3d',
            field=models.ImageField(blank=True, null=True, upload_to='structures/3d/'),
        ),
        migrations.AlterField(
            model_name='lipopeptidediscoverdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 9, 4, 46, 876336, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidediscoverdata',
            name='discoverer_image',
            field=models.ImageField(blank=True, null=True, upload_to='discoverer/'),
        ),
        migrations.AlterField(
            model_name='lipopeptidefunctionsdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 9, 4, 46, 874040, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptideliganddata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 9, 4, 46, 874769, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidemetabolismdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 9, 4, 46, 877272, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidepathwaydata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 9, 4, 46, 875487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidepathwaydata',
            name='lipopeptide_pathway_image',
            field=models.ImageField(blank=True, null=True, upload_to='pathways/'),
        ),
        migrations.AlterField(
            model_name='lipopeptidepropertiesdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 9, 4, 46, 877964, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lipopeptidereferencesdata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 9, 4, 46, 878616, tzinfo=utc)),
        ),
    ]