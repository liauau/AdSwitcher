# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switcher', '0015_auto_20170622_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='latest_version',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]