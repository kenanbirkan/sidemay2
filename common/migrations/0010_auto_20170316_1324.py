# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 13:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_auto_20170316_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit',
            name='name',
        ),
        migrations.RemoveField(
            model_name='credit',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='dues_dernek',
            name='name',
        ),
        migrations.RemoveField(
            model_name='dues_dernek',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='dues_sandik',
            name='name',
        ),
        migrations.RemoveField(
            model_name='dues_sandik',
            name='surname',
        ),
        migrations.AlterField(
            model_name='profile',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 16, 13, 24, 49, 547186)),
        ),
    ]