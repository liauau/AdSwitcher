# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-27 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switcher', '0033_auto_20171210_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='cracknode',
            name='gp',
            field=models.IntegerField(default=0),
        ),
    ]
