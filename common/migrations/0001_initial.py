# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('tc', models.CharField(max_length=12)),
                ('value', models.IntegerField(default=0)),
                ('insert_date', models.DateTimeField(verbose_name='date started')),
            ],
        ),
        migrations.CreateModel(
            name='Dues_Dernek',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('tc', models.CharField(max_length=12)),
                ('value', models.IntegerField(default=0)),
                ('insert_date', models.DateTimeField(verbose_name='date started')),
            ],
        ),
        migrations.CreateModel(
            name='Dues_Sandik',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('tc', models.CharField(max_length=12)),
                ('value', models.IntegerField(default=0)),
                ('insert_date', models.DateTimeField(verbose_name='date started')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('tc', models.CharField(max_length=12)),
                ('dues_sandik', models.IntegerField(default=0)),
                ('dues_dernek', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=200)),
                ('grup', models.IntegerField(default=0)),
                ('start_date', models.DateTimeField(verbose_name='date started')),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('info', models.CharField(max_length=200)),
                ('value', models.IntegerField(default=0)),
                ('insert_date', models.DateTimeField(verbose_name='date started')),
            ],
        ),
    ]
