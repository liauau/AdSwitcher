# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 02:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('switcher', '0003_auto_20170527_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='context',
            name='signatures',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='placement',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placements', to='switcher.AppNode'),
        ),
    ]