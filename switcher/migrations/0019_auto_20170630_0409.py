# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-30 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switcher', '0018_auto_20170628_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='crackplacement',
            name='max_times',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='crackplacement',
            name='start_times',
            field=models.IntegerField(default=0),
        ),
    ]
