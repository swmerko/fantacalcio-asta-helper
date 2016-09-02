# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='fanta_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='sold_value',
            field=models.IntegerField(null=True),
        ),
    ]